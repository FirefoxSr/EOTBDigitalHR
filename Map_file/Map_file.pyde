import Encounters
import json
def setup():
    global mapImage, enemy, currentPlayer, p1Image, p2Image
    fullScreen()
    size(1920, 1080)
    mapImage = loadImage("map.png")
    p1Image = loadImage("p1.png")
    p2Image = loadImage("p2.png")
    imageMode(CENTER)
    font = loadFont("font.vlw")
    textSize(40)
    ellipseMode(CENTER)
    enemy = ''
    currentPlayer = p1Image
def draw():
    global mapImage, enemy, playerImage
    background(0)
    image(mapImage, 400, height // 2)
    message = 'Please click on the square you landed.'
    text(message, 800, 200)
    text(str(enemy),800,700)
    currentPlayer = 'p1'
    if currentPlayer == 'p1':
        currentPlayerImage = p1Image
    else:
        currentPlayerImage = p2Image
    def playerImage(x,y):
        global p1Image, p2Image, currentPlayer
        x = x + 16
        y = y + 16
        image(currentPlayerImage,x,y)
        
    """
    #1
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #2
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #3
    ellipse()
    ellipse()
    ellipse()
    #4
    ellipse()
    ellipse()
    #5
    ellipse()
    ellipse()
    ellipse()
    #6
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #7
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #8
    ellipse()
    ellipse()
    ellipse()
    #9
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #10
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #11
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #12
    ellipse()
    #13
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #14
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #15
    ellipse()
    #16
    ellipse()
    ellipse()
    #17
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #18
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #19
    ellipse()
    #20
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #21
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    ellipse()
    #22
    ellipse()
    """

 
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mouseClicked():
    global enemy, currentPlayer, p1Image, p2Image, playerImage
    if isMouseWithinSpace(96,941,32,32):
        playerImage(96,941)
        enemy = Encounters.encounters(1)
