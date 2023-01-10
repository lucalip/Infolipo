# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:12:36 2023

@author: Maintenant prêt !
"""



import pygame
import numpy as np
import time

# Initialisation de la fenêtre
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jeu de la vie')

# Initialisation des variables
running = True
grid = np.zeros((800, 600))

# Boucle principale

# Détection des sons
sound = pygame.mixer.Sound('sound.wav')
sound.play()
amplitude = sound.get_volume()
frequency = sound.get_frequency()
silence = sound.get_length()
variation = sound.get_endevent()

# Mise à jour de la grille
if amplitude > 0.5:
grid[frequency][silence] = 1
elif amplitude < 0.5:
grid[frequency][silence] = 0
if variation > 0.5:
grid[frequency][silence] = 0
elif variation < 0.5:
grid[frequency][silence] = 1

# Mise à jour de l'affichage
screen.fill((0, 0, 0))
for x in range(800):
for y in range(600):
if grid[x][y] == 1:
pygame.draw.rect(screen, (255, 255, 255), (x, y, 1, 1))
pygame.display.flip()

# Gestion des événements
for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False

pygame.quit()
