import pygame
TITLE = "Flappy Bird game"
WIDTH = 800
HEIGHT = 700
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
        super().__init__()
        self.images = [b1,b2,b3]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.vy = 0
    def update(self):
        self.counter += 1
        if self.counter > 10:
            self.counter = 0
            self.index += 1
            if self.index > 2:
                self.index = 0
            self.image = self.images[self.index]
        if self.vy < 5:
            self.vy += 0.05
        self.rect.y += self.vy
        if pygame.mouse.get_pressed()[0]:
            self.vy = -3




bird = Flappybird(100,300)
birdgroup = pygame.sprite.Group()
birdgroup.add(bird)




groundx = 0
while run == True:
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    bird.update()
    screen.blit(g,(groundx,600))
    groundx -= 1
    if groundx < -100:
        groundx = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()