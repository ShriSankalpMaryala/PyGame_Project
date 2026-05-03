import random
import pygame
WIDTH = 600
HEIGHT = 600
TITLE = "Pygame_Shapes_and_Events"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
while run == True:
    screen.fill("blue")
    for event in pygame.event.get():
        pass
    pygame.display.update()