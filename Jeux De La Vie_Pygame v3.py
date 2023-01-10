# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:22:40 2023

@author: Maintenant prêt !
"""

import pygame
import random

# Initialisation de pygame
pygame.init()

# Définition des couleurs
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Définition des instruments
instruments = [
    pygame.mixer.Sound("instrument1.wav"),
    pygame.mixer.Sound("instrument2.wav"),
    pygame.mixer.Sound("instrument3.wav"),
    pygame.mixer.Sound("instrument4.wav")
]

# Définition des couleurs associées aux instruments
colors = [RED, GREEN, BLUE, BLACK]

# Définition des amplitudes
amplitudes = [0.1, 0.2, 0.3, 0.4]

# Définition des fréquences
frequencies = [220, 440, 880, 1760]

# Définition des silences
silences = [0.1, 0.2, 0.3, 0.4]

# Définition des variations de sons
variations = [0.1, 0.2, 0.3, 0.4]

# Boucle principale
while 
    # Choix aléatoire d'un instrument
    instrument = random.choice(instruments)
    # Choix aléatoire d'une couleur
    color = random.choice(colors)
    # Choix aléatoire d'une amplitude
    amplitude = random.choice(amplitudes)
    # Choix aléatoire d'une fréquence
    frequency = random.choice(frequencies)
    # Choix aléatoire d'un silence
    silence = random.choice(silences)
    # Choix aléatoire d'une variation de son
    variation = random.choice(variations)
    # Jouer l'instrument
    instrument.play(amplitude, frequency, silence, variation)
    # Dessiner la couleur associée à l'instrument
    pygame.draw.rect(screen, color, (0, 0, width, height))
    # Mise à jour de l'écran
    pygame.display.flip()
