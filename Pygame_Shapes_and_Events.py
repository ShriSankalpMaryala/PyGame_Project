import random
import pygame
WIDTH = 600
HEIGHT = 600
TITLE = "Pygame_Shapes_and_Events"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
run = True
class Circle():
    def __init__(self,s,c,x,y):
        self.size = s
        self.colour = c
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.circle(screen,self.colour,(self.x,self.y), self.size)
ball = Circle(20, "green", 200, 400)




while run == True:
    screen.fill("blue")
    ball.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.size += 5
        if event.type == pygame.MOUSEBUTTONUP:
            ball.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            ball.x,ball.y = pos




    pygame.display.update()
