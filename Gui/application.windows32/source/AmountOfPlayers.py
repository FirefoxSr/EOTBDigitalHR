def setup():
    fullScreen()
    textAlign(CENTER)
    rectMode(CENTER)
    noFill()
def draw():
    text("Do you want to play with 1 or 2 players?",width // 3, 200)
    rect(635, 845, 200, 65)
    rect(1275, 845, 225, 65)
    text("1 player",640, height - 270)
    text("2 players",1280, height - 270)
    
def isMouseWithinSpace(x,y,w,h):
        if (x < mouseX < x + w and y < mouseY < y + h):
            return True
        else:
            return False

AmountOfPlayers = 0        
def mousePressed():
    global screen, AmountOfPlayers
    if isMouseWithinSpace(640, 1650, 200, 100):
        screen = "Map"
        AmountOfPlayers = 1
    if isMouseWithinSpace(1275, 845, 225, 65):
        AmountOfPlayers = 2
    
    
    
