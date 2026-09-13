"""Protocole UDP temps reel et watchdog de perte de flux."""

from dataclasses import dataclass
import json
import socket
import time


PROTOCOL_VERSION = 1
PACKET_RATE_HZ = 50
HOLD_TIMEOUT_S = 0.100
STOP_TIMEOUT_S = 0.500


@dataclass(frozen=True)
class CommandPacket:
    frame_id: int
    timestamp_ns: int
    pressure: int

    def encode(self) -> bytes:
        """Encode une trame compacte et deterministe."""
        return (json.dumps({
            "v": PROTOCOL_VERSION,
            "frame_id": self.frame_id,
            "timestamp_ns": self.timestamp_ns,
            "pressure": self.pressure,
        }, separators=(",", ":"), sort_keys=True) + "\n").encode("ascii")

    @classmethod
    def decode(cls, payload: bytes) -> "CommandPacket":
        try:
            value = json.loads(payload.decode("ascii"))
            if value.get("v") != PROTOCOL_VERSION:
                raise ValueError("version de protocole inconnue")
            frame_id = value["frame_id"]
            timestamp_ns = value["timestamp_ns"]
            pressure = value["pressure"]
            if not isinstance(frame_id, int) or frame_id < 0:
                raise ValueError("frame_id invalide")
            if not isinstance(timestamp_ns, int) or timestamp_ns <= 0:
                raise ValueError("timestamp invalide")
            if not isinstance(pressure, int) or not 0 <= pressure <= 10:
                raise ValueError("pression invalide")
            return cls(frame_id, timestamp_ns, pressure)
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            raise ValueError("paquet UDP invalide") from exc


class StreamWatchdog:
    """Ignore les doublons/retards et applique hold puis stop sans saut."""

    def __init__(self, clock=time.monotonic):
        self._clock = clock
        self.last_frame_id = None
        self.last_packet_time = None
        self.last_pressure = 0
        self.mode = "stop"

    def accept(self, packet: CommandPacket) -> bool:
        now = self._clock()
        if self.last_frame_id is not None and packet.frame_id <= self.last_frame_id:
            return False
        self.last_frame_id = packet.frame_id
        self.last_packet_time = now
        self.last_pressure = packet.pressure
        self.mode = "run"
        return True

    def command(self):
        if self.last_packet_time is None:
            self.mode = "stop"
            return "stop", 0
        elapsed = self._clock() - self.last_packet_time
        if elapsed > STOP_TIMEOUT_S:
            self.mode = "stop"
            return "stop", 0
        if elapsed > HOLD_TIMEOUT_S:
            self.mode = "hold"
            return "hold", self.last_pressure
        self.mode = "run"
        return "run", self.last_pressure


class UdpCommandSender:
    """Emet une consigne numerotee; appeler send() a 50 Hz."""

    def __init__(self, address, sock=None, clock=time.monotonic_ns):
        self.address = address
        self.sock = sock or socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._clock = clock
        self.frame_id = 0

    def send(self, pressure: int) -> int:
        """Envoie une trame et retourne son identifiant."""
        packet = CommandPacket(self.frame_id, self._clock(), pressure)
        self.sock.sendto(packet.encode(), self.address)
        sent_id = self.frame_id
        self.frame_id += 1
        return sent_id

    def close(self):
        self.sock.close()