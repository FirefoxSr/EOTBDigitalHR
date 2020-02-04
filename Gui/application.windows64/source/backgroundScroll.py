def setup():
    global backGround, x
    frameRate(90)
    backGround = loadImage("Background.png")
    image(backGround,0,0)
    x = 2560
def draw():
    global backGround, x
    imageMode(CENTER)
    x = x - 1
    image(backGround, x, height // 2)
    if (x < 0):
        x = 2560
