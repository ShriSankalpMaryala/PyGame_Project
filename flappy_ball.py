import pgzrun
TITLE = "Flappy Ball Game"
WIDTH = 600
LENGTH = 600
GRAVITY = 500
class Ball():
    def __init__(self, c, r, x, y):
        self.color = c
        self.radius = r
        self.x = x
        self.y = y
        self.vx = 40
        self.vy = 0
    def draw(self):
        screen.draw.filled_circle((self.x,self.y), self.radius, self.color)

bouncyball = Ball("red", 12, 300, 300)


        

def draw():
    screen.fill("blue")
    bouncyball.draw()


def update(dt):
    uy = bouncyball.vy
    bouncyball.vy += GRAVITY * dt
    bouncyball.y += (uy + bouncyball.vy) * 0.5 * dt
    bouncyball.x += bouncyball.vx * dt
    if bouncyball.y > 600 - bouncyball.radius:
        bouncyball.vy *= -1
    if bouncyball.x > 600 - bouncyball.radius:
        bouncyball.vx *= -1
    if bouncyball.x <bouncyball.radius:
        bouncyball.vx *= -1
    if bouncyball.y <bouncyball.radius:
        bouncyball.vy *= -1








pgzrun.go()
