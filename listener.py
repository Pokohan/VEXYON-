import socket
import pygame
import sys

from udp_protocol import CommandPacket, StreamWatchdog

# --- CONFIGURATION RÉSEAU ---
UDP_IP = "0.0.0.0"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(False) # Pour ne pas figer l'écran en attendant les données
sock.bind((UDP_IP, UDP_PORT))
watchdog = StreamWatchdog()

# --- CONFIGURATION GRAPHIQUE ---
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("VEXYON - Simulateur de Pince")
clock = pygame.time.Clock()

pression = 0
mode = "stop"

while True:
    screen.fill((30, 30, 30)) # Fond gris foncé
    
    # 1. Vérifier si on reçoit des données
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            try:
                packet = CommandPacket.decode(data)
            except ValueError:
                continue
            if watchdog.accept(packet):
                pression = packet.pressure
    except BlockingIOError:
        pass # Aucun paquet disponible ce tour-ci

    mode, pression = watchdog.command()

    # 2. Gérer la fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 3. DESSINER LE BRAS / LA PINCE
    # On change l'ouverture selon la pression
    ouverture = 100 - (pression * 30) # Plus la pression est forte, plus c'est serré
    
    # Dessin de la base
    pygame.draw.rect(screen, (100, 100, 100), (180, 300, 40, 100))
    
    # Dessin des mâchoires de la pince (Couleur change selon la pression)
    couleur = (0, 255, 0) # Vert par défaut
    if mode == "hold": couleur = (255, 165, 0)
    if mode == "stop": couleur = (255, 0, 0)
    if pression == 2: couleur = (255, 165, 0) # Orange
    if pression >= 3: couleur = (255, 0, 0)   # Rouge
    
    # Mâchoire gauche
    pygame.draw.rect(screen, couleur, (150 - (ouverture//2), 200, 20, 100))
    # Mâchoire droite
    pygame.draw.rect(screen, couleur, (230 + (ouverture//2), 200, 20, 100))

    pygame.display.flip()
    clock.tick(50)
