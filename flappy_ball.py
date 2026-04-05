import pgzrun
TITLE = "Flappy Ball Game"
WIDTH = 600
LENGTH = 600
class Ball():
    def __init__(self, c, r, x, y):
        self.color = c
        self.radius = r
        self.x = x
        self.y = y
    def draw(self):
        screen.draw.filled_circle((self.x,self.y), self.radius, self.color)

bouncyball = Ball("red", 12, 300, 300)


        

def draw():
    screen.fill("blue")
    bouncyball.draw()


def update():
    pass
pgzrun.go()
