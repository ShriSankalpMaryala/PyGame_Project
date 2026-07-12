import pygame
TITLE = "Flappy Bird game"
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
b1 = pygame.image.load("flappy bird.png")
obstacle = pygame.image.load("obstacle.png")
bg = pygame.image.load("background.png")
b2 = pygame.image.load("flappy bird 1.png")
b3 = pygame.image.load("flappy bird 2.png")
g = pygame.image.load("ground.png")
class Flappybird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.images = [b1,b2,b3]
        self.index = 0
        self.image = self.images[self.index]






while run == True:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()