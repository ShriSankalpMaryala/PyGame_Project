import pygame
pygame.init()
TITLE = "Flappy Bird game"
WIDTH = 800
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
b1 = pygame.image.load("flappy bird.png")
o = pygame.image.load("obstacle.png")
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
        if gameover == False:
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
            if pygame.mouse.get_pressed()[0]and gameover == False:
                self.vy = -1
gameover = False
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,image,x,y,flag):
        super().__init__()
        self.image = image
        if flag == 20:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.bottom = y
        if flag == 40:
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


       
    def update(self):
        global score
        self.rect.x -= 1
        if self.rect.x == 100:
            score += 0.5
        if self.rect.x < -50:
            self.kill()




pipegroup = pygame.sprite.Group()

bird = Flappybird(100,300)
birdgroup = pygame.sprite.Group()
birdgroup.add(bird)




groundx = 0
pipefrequency = 3000
lastpipe = 0
score = 0
while run == True:
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    pipegroup.draw(screen)
    bird.update()
    font = pygame.font.SysFont("Arial",20)
    text = font.render("Score:" + str(score),True,"Blue")
    screen.blit(text,(0,0))
    if pygame.sprite.groupcollide(birdgroup,pipegroup,False,False):
        gameover = True
    timenow = pygame.time.get_ticks()
    print(timenow)
    if gameover == True:
        font = pygame.font.SysFont("Arial",50)
        text = font.render("Game Over",True,"Red")
        screen.blit(text,(300,400))
    if timenow - lastpipe > pipefrequency and gameover == False:
    

        pipe = Obstacle(o,800,450,40)
        pipe2 = Obstacle(o,800,250,20)
        pipegroup.add(pipe)
        pipegroup.add(pipe2)
        lastpipe = timenow
        print(timenow)
    screen.blit(g,(groundx,600))
    if gameover == False:
        pipegroup.update()
        groundx -= 1
    if groundx < -100:
        groundx = 0
    if len(pipegroup)>0:
        if pygame.sprite.groupcollide(birdgroup,pipegroup,False,False):
            gameover = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()