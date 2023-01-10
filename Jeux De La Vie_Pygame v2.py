# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:21:07 2023

@author: Maintenant prêt !
"""

import pygame
import random

# Initialisation de la fenêtre
pygame.init()

# Définition des constantes
WIDTH = 800
HEIGHT = 600

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Création de la grille
grid = []
for row in range(10):
grid.append([])
for column in range(10):
grid[row].append(0)

# Définition des variables
running = True

# Boucle principale
while 
# Récupération des événements
for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False

# Récupération de la musique
music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

# Mise à jour de la grille
for row in range(10):
for column in range(10):
if random.randint(0, 1) == 0:
grid[row][column] = 0
else:
grid[row][column] = 1

# Dessin de la grille
for row in range(10):
for column in range(10):
color = WHITE
if grid[row][column] == 1:
color = BLACK
pygame.draw.rect(screen, color, [(WIDTH // 10) * column, (HEIGHT // 10) * row, WIDTH // 10, HEIGHT // 10])

# Mise à jour de l'écran
pygame.display.flip()

# Fermeture de la fenêtre
pygame.quit()
