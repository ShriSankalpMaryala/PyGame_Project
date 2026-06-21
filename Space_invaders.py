import pygame
TITLE = "Space Invaders"
HEIGHT = 600
WIDTH = 1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
bg1 = pygame.image.load("yellow_spaceship.png")
bg2 = pygame.image.load("red_spaceship.png")
bg3 = pygame.image.load("milky way.png")
bg3 = pygame.transform.scale(bg3,(1000,600)) 



class Spaceship(pygame.sprite.Sprite):
     def __init__ (self,image,x,y,angle):
          super().__init__()
          self.image = image
          self.image = pygame.transform.scale(self.image,(70,70))
          self.image = pygame.transform.rotate(self.image, angle)
          self.rect = self.image.get_rect()
          self.rect.x = x
          self.rect.y = y

          
redship = Spaceship(bg2,150,150,90)
yellowship = Spaceship(bg1,500,500,270)
shipgroup = pygame.sprite.Group()
shipgroup.add(yellowship)
shipgroup.add(redship)



while True:
    screen.blit(bg3,(0,0))
    shipgroup.draw(screen)
    pygame.draw.line(screen,"white",(500,0),(500,600))
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              run = False
    
























    pygame.display.update()
   


