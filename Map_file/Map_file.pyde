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
        
   
#this function makes it easy to see wether or not you clicked on a certain area of the screen 
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
#here we execute a function if the user clicks on squares on the map
def mouseClicked():
    global enemy, currentPlayer, p1Image, p2Image, playerImage
    if isMouseWithinSpace(96,941,32,32):
        playerImage(96,941)
        enemy = Encounters.encounters(1)
