import Combat
import Map
import Encounters
import json
import AmountOfPlayers
import ScreenTitle
import Crafting
import backgroundScroll
import Combat_screen


def setup():
    global screen, x, y, w, h, backGround
    fullScreen()
    frameRate(60)
    backGround = loadImage("Background.jpg")
    screen = "titleScreen"
    ScreenTitle.setup()
    AmountOfPlayers.setup()
    backgroundScroll.setup()
    Combat_screen.setup()
    Map.setup()
    ScreenTitle.setup()
    Crafting.setup()

    

        
def draw():
    global screen, backGround, amountOfPlayers
    if (screen == "titleScreen"):
        backgroundScroll.draw()
        ScreenTitle.draw()
    if (screen == "playerScreen"):
        background(0)
        backgroundScroll.draw()
        AmountOfPlayers.draw()
    if (screen == "combat"):
        background(0)
        imageMode(CORNER)
        backgroundScroll.draw()
        Combat_screen.draw()
    if (screen == "combat2"):
        background(0)
        imageMode(CORNER)
        backgroundScroll.draw()
        textAlign(CORNER)
        Combat_screen.draw()
        Combat.endOfCombat
    if (screen == "Map"):
        background(0)
        backgroundScroll.draw()
        imageMode(CENTER)
        Map.draw()
        textAlign(LEFT)
        noTint()
    if (screen == "Crafting"):
        background(0)
        imageMode(CENTER)
        backgroundScroll.draw()
        imageMode(CORNER)

    print(screen)

        
        
def isMouseWithinSpace(x,y,w,h):
        if (x < mouseX < x + w and y < mouseY < y + h):
            return True
        else:
            return False
def mouseClicked():
    global screen, x, y, w, h, amountOfPlayers
    if (screen == "titleScreen"):
        if isMouseWithinSpace(750, 660, 858, 150):
            screen = "playerScreen"        
    if (screen == "playerScreen"):
        if isMouseWithinSpace(527,801,233,88):
            amountOfPlayers = 1
            screen = "Map"
        if isMouseWithinSpace(1151,799,233,88):
            amountOfPlayers = 2
            screen = "Map"
    if (screen == "combat"):
        Combat_screen.mouseClicked()
        imageMode(CORNER)
        textMode(CORNER)
        rectMode(CORNER)
        if isMouseWithinSpace(95, 970, 305, 60):
            screen = "Map"
    if (screen == "combat"):
        if isMouseWithinSpace(95, 970, 305, 60):
            Map.setup()
            screen = "Map"
    if (screen == "Map"):
        Map.isMouseWithinSpace
        Map.mouseClicked()
        if Map.currentPlayer == 2:
            if isMouseWithinSpace(1488,931,186,58):
                screen = "combat"
        if Map.currentPlayer == 1:
            if isMouseWithinSpace(1488,931,186,58):
                screen = "combat"
            
        if (screen == "Map"):
            if isMouseWithinSpace(800,925,366,78):
                screen = "Crafting"
                Crafting.draw()
                Crafting.screen = 0
    if (screen == "Crafting"):
        if isMouseWithinSpace(150, 100, 150, 60):
            screen = "Map"
        Crafting.isMouseWithinSpace
        Crafting.mousePressed()
        Crafting.draw()
        
    if Combat_screen.screen == 'No_Encounter':
        if isMouseWithinSpace(0, 0, 1920, 1080):
            textSize(50)
            imageMode(CORNER)
            screen = 'Map'
            
    
        
        
