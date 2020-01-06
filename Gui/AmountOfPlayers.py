def setup():
    fullScreen()
    textAlign(CENTER)
def draw():
    text("Do you want to play with 1 or 2 players?",width // 4, 200)
    
    
    text("1 player",640, height - 270)
    text("2 players",1280, height - 270)
#screen = "PlayerScreen"
    
def isMouseWithinSpace(x,y,w,h):
        if (x < mouseX < x + w and y < mouseY < y + h):
            return True
        else:
            return False

AmountOfPlayers = 0        
def mousePressed():
    global screen, AmountOfPlayers
    if isMouseWithinhSpace(640, height - 270, 200, 100):
        screen = "Map"
        AmountOfPlayers = 1
    
    
    
