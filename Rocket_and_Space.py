import pygame
import random
TITLE = "Rocket in Space"
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg1 = pygame.image.load("rocket.png")
bg2 = pygame.image.load("milky way.png")
rocket_x = 300
rocket_y = 300
run = True
while run == True:
    screen.blit(bg2,(0,0))
    screen.blit(bg1,(rocket_x,rocket_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                rocket_x -= 10
            if event.key == pygame.K_w:
                rocket_y -= 10
            if event.key == pygame.K_s:
                rocket_y += 10
            if event.key == pygame.K_d:
                rocket_x += 10
    
    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_UP]:
        rocket_y -= 2
    if keypressed[pygame.K_DOWN]:
        rocket_y += 2
    if keypressed[pygame.K_LEFT]:
        rocket_x -= 2
    if keypressed[pygame.K_RIGHT]:
        rocket_x += 2

    if rocket_y < 0:
        rocket_y = 0  
    
    if rocket_x < 0:
        rocket_x = 0

            
            
            
            

    pygame.display.update()





