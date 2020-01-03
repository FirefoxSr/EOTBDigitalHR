import Combat
import Map
import Encounters
import json
import playerScreen
import titleScreen



def setup():
    global screen, x, y, w, h
    fullScreen()
    screen = "titleScreen"
    titleScreen.setup()
    playerScreen.setup()
    Combat.setup()
    Map.setup()

def draw():
    global screen
    if (screen == "titleScreen"):
        titleScreen.draw()
    if (screen == "playerScreen"):
        playerScreen.draw()
    if screen == "combat":
        Combat.draw()
    elif screen == "Map":
        Map.draw()
        tint(255,255)
        
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
        if (1550 < mouseX < 1865 and 944 < mouseY < 1144):
            screen = "Map"
    if (screen == "combat"):
        Combat.isMouseWithinSpace
        Combat.mousePressed()
    if (screen == "Map"):
        Map.isMouseWithinSpace
        Map.mouseClicked()
        if isMouseWithinSpace(1488,931,186,58):
            screen = "combat"
    
        
        
