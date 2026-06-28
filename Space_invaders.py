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
redbullets = []
yellowbullets = []



while True:
     screen.blit(bg3,(0,0))
     shipgroup.draw(screen)
     pygame.draw.line(screen,"white",(500,0),(500,600))
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_e:
                    bullet = pygame.Rect(redship.rect.right,redship.rect.top+30,20,10)
                    redbullets.append(bullet)
                    







     keypressed = pygame.key.get_pressed()
     if keypressed[pygame.K_w]:
          redship.rect.y -= 1
     if keypressed[pygame.K_a]:
          redship.rect.x -= 1
     if keypressed[pygame.K_s]:
          redship.rect.y += 1
     if keypressed[pygame.K_d]:
          redship.rect.x += 1
     if keypressed[pygame.K_UP]:
          yellowship.rect.y -= 1
     if keypressed[pygame.K_LEFT]:
          yellowship.rect.x -= 1
     if keypressed[pygame.K_DOWN]:
          yellowship.rect.y += 1
     if keypressed[pygame.K_RIGHT]:
          yellowship.rect.x += 1
     
     if redship.rect.top < 0:
          redship.rect.top = 0
     if redship.rect.left < 0:
          redship.rect.left = 0
     if redship.rect.bottom > 600:
          redship.rect.bottom = 600
     if redship.rect.right > 500:
          redship.rect.right = 500
     
     if yellowship.rect.top < 0:
          yellowship.rect.top = 0
     if yellowship.rect.left < 500:
          yellowship.rect.left = 500
     if yellowship.rect.bottom > 600:
          yellowship.rect.bottom = 600
     if yellowship.rect.right > 1000:
          yellowship.rect.right = 1000
     


    









     pygame.display.update()
   


