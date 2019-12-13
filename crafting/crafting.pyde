def setup():
    fullScreen()
    global foto1
    foto1 = loadImage("Basic_Spear.png")
        
def draw():
    global foto1
    background(0,0,0)
    textSize(52)
    textAlign(CENTER)
    text(foto1, 300, 200)
