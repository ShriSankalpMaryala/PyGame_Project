import pygame
import random
pygame.init()
pygame.mixer.init()
music = pygame.mixer.Sound("Happy Birthday Song.mp3")
TITLE = "Birthday Animation"
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
bg1 = pygame.image.load("balloon.jpg")
bg2 = pygame.image.load("cake.jpg")
bg3 = pygame.image.load("present.jpg")
run = True
music.play(-1)
while run == True:
    screen.blit(bg1,(0,0))
    font = pygame.font.SysFont("Arial",24)
    text = font.render("Happy Birthday", True, "Blue")
    screen.blit(text,(250,300))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(bg2,(0,0))
    font = pygame.font.SysFont("Arial",30)
    text = font.render("Many Happy Returns", True, "Red")
    screen.blit(text,(100,100))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(bg3,(0,0))
    font = pygame.font.SysFont("Arial",45)
    text = font.render("Have a great day", True, "Yellow")
    screen.blit(text,(100,100))
    pygame.display.update()
    pygame.time.delay(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()


        