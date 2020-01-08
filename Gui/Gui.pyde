import Combat
import Map
import Encounters
import json
import test
import AmountOfPlayers
import ScreenTitle
import Crafting
import Combat2
import backgroundScroll

def setup():
    global screen, x, y, w, h, backGround
    fullScreen()
    frameRate(60)
    backGround = loadImage("Background.jpg")
    screen = "titleScreen"
    Combat.setup()
    Map.setup()
    AmountOfPlayers.setup()
    ScreenTitle.setup()
    Crafting.setup()
    Combat2.setup()
    backgroundScroll.setup()
        
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
        imageMode(CENTER)
        backgroundScroll.draw()
        textAlign(CENTER)
        imageMode(CORNER)
        Combat.draw()
        Combat.endOfCombat
    if (screen == "combat2"):
        background(0)
        imageMode(CENTER)
        backgroundScroll.draw()
        textAlign(CENTER)
        imageMode(CORNER)
        Combat2.draw()
        Combat.endOfCombat
    if (screen == "Map"):
        background(0)
        backgroundScroll.draw()
        if (amountOfPlayers == 2):
            text("Switch to next player",200,1050) 
        imageMode(CENTER)
        Map.draw()
        textAlign(LEFT)
        noTint()
    if (screen == "Crafting"):
        background(0)
        imageMode(CENTER)
        backgroundScroll.draw()
        imageMode(CORNER)
        Crafting.draw()
    print(screen)
        
def isMouseWithinSpace(x,y,w,h):
        if (x < mouseX < x + w and y < mouseY < y + h):
            return True
        else:
            return False
def mousePressed():
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
        Combat.isMouseWithinSpace
        Combat.mousePressed()
        if isMouseWithinSpace(0,0,300,66):
            screen = "Map"
    if (screen == "combat2"):
        Combat2.isMouseWithinSpace
        Combat2.mousePressed()
        if isMouseWithinSpace(0,0,300,66):
            screen = "Map"
    if (screen == "Map"):
        Map.isMouseWithinSpace
        Map.mousePressed()
        if (amountOfPlayers == 2):
            if (isMouseWithinSpace,200,1050,518,63):
                Map.endTurn = True
                Map.currentPlayer = Map.playerTurn(Map.currentPlayer)
        if Map.currentPlayer == 2:
            if isMouseWithinSpace(1488,931,186,58):
                screen = "combat"
        elif Map.currentPlayer == 1:
            if isMouseWithinSpace(1488,931,186,58):
                screen = "combat2"
            
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
        
            
    
        
        
