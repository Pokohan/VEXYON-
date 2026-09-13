import numpy as np


def extract_pressure_features(landmarks, prev_pos=None, dt=1.0):
    """
    Extrait les traits de pression dans le même format que la démo
    de webcam : positions relatives au landmark racine, puis normalisées
    par taille de main pour rendre l'échelle cohérente avec le flux live.
    """
    points = getattr(landmarks, "landmark", landmarks)
    coords = np.array([[lm.x, lm.y, lm.z] for lm in points], dtype=np.float32)

    relative_pos = coords - coords[0]
    hand_size = max(np.linalg.norm(relative_pos, axis=1).max(), 1e-8)
    pos = relative_pos / hand_size

    if prev_pos is not None:
        dt_safe = max(float(dt), 1e-6)
        vel = (pos - prev_pos) / dt_safe
    else:
        vel = np.zeros_like(pos)

    features = np.concatenate([pos.flatten(), vel.flatten()])
    return features, pos
