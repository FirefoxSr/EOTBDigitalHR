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
    rect(234,896,31,29)
        
   
#this function makes it easy to see wether or not you clicked on a certain area of the screen 
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
#here we execute a function if the user clicks on squares on the map, this is gona be a long one. Just bear with me ^^
def mouseClicked():
    global enemy, currentPlayer, p1Image, p2Image, playerImage
    if isMouseWithinSpace(132,933,32,228):
        enemy = Encounters.encounters(1)

    if isMouseWithinSpace(167,951,31,28):
            enemy = Encounters.encounter(1)
    if isMouseWithinSpace(184,912,31,30):
        enemy = Encounters.encounter(1)
    if isMouseWithinSpace(138,894,32,29):
        enemy = Encounters.encounter(1)
    if isMouseWithinSpace(286,883,31,29):
        enemy = Encounters.encounter(1)
    if isMouseWithinSpace(234,896,31,29):
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()
    if isMouseWithinSpace():
        enemy = Encounters.encounter()

    
