def setup():
    global backGround, x
    frameRate(60)
    backGround = loadImage("Background.png")
    x = 0
def draw():
    global backGround, x

    x = x - 1
    image(backGround, x, height // 2)
    print(x)
    if (x < -1080):
        x = width // 2
