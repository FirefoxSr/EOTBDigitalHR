import Combat
import Map
import Encounters
import json
import test
import AmountOfPlayers
import ScreenTitle
import Crafting

def setup():
    global screen, x, y, w, h
    fullScreen()
    screen = "titleScreen"
    Combat.setup()
    Map.setup()
    AmountOfPlayers.setup()
    ScreenTitle.setup()
    Crafting.setup()

def draw():
    global screen
    if (screen == "titleScreen"):
        background(0)
        ScreenTitle.draw()
    if (screen == "playerScreen"):
        background(0)
        AmountOfPlayers.draw()
    if (screen == "combat"):
        background(0)
        Combat.draw()
    if (screen == "Map"):
        background(0)
        Map.draw()
        textAlign(LEFT)
        
        noTint()
    if (screen == "Crafting"):
        background(0)
        Crafting.draw()
    print(screen)
    rect(250,100,155,60)
        
def isMouseWithinSpace(x,y,w,h):
        if (x < mouseX < x + w and y < mouseY < y + h):
            return True
        else:
            return False
def mousePressed():
    global screen, x, y, w, h
    if (screen == "titleScreen"):
        if isMouseWithinSpace(1000, 660, 608, 150):
            screen = "playerScreen"
            
    if (screen == "playerScreen"):
        if isMouseWithinSpace(1550,844,315,200):
            screen = "Map"
    if (screen == "combat"):
        Combat.isMouseWithinSpace
        Combat.mousePressed()
    if (screen == "Map"):
        Map.isMouseWithinSpace
        Map.mouseClicked()
        if isMouseWithinSpace(1488,931,186,58):
            screen = "combat"
        if (screen == "Map"):
            if isMouseWithinSpace(800,925,366,78):
                screen = "Crafting"
        if (screen == "Crafting"):
            if isMouseWithinSpace(250,100,155,60):
                screen = "Map"
                
    
        
        
