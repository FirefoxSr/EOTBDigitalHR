def setup():
    global font, score, message, img
    size(800,800)
    message = "score" 
    score = 0
    img = loadImage("deepfry.png")
    

def draw():
    global message, font, img
    background(100)
    font = loadFont("lmao.vlw")
    textFont(font, 32)
    fill(100, 0, 0)
    text(message, width/2, 100)
    text(int(score), width/2, 140)
    image(img, width/2, height/2)


def mousePressed():
    global score
    score = score + 1

input()
