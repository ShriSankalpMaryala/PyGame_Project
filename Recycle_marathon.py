import pygame
import random
TITLE = "Recycle Marathon"
WIDTH = 1000
LENGTH = 800
screen = pygame.display.set_mode((WIDTH,LENGTH))
run = True
g = pygame.image.load("ground.png")
p = pygame.image.load("pencil.png")
pb = pygame.image.load("paper bag.png")
b = pygame.image.load("box.png")
bi = pygame.image.load("bin.png")
bg = pygame.image.load("background.png")
plb = pygame.image.load("plastic bag.png")

class Bin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.transform.scale(bi,(50,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Plastic_Bag(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.transform.scale(plb,(40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Recyclable_Items(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images = [p,pb,b]
        self.image = random.choice(self.images)
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    

bingroup = pygame.sprite.Group()
bin = Bin(0,0)
bingroup.add(bin)

plastic_baggroup = pygame.sprite.Group()
for i in range(20):
    plastic_bag = Plastic_Bag(random.randint(0,900),random.randint(0,700))
    plastic_baggroup.add(plastic_bag)

recyclable_itemsgroup = pygame.sprite.Group()
for i in range(35):
    recyclable_items = Recyclable_Items(random.randint(0,900),random.randint(0,700))
    recyclable_itemsgroup.add(recyclable_items)

    

while run == True:
    screen.blit(bg,(0,0))
    bingroup.draw(screen)
    plastic_baggroup.draw(screen)
    recyclable_itemsgroup.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()