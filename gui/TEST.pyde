import Startscherm, playerScherm

def setup():
    global screen
    size(1280,720)
    
    screen = 'Startscherm'
    playerScherm.setup()
    Startscherm.setup()
    
def draw():
    global screen
    if screen == 'Startscherm':
        Startscherm.draw()
    
    elif screen == 'playerScherm':
        playerScherm.draw()
    

def mousePressed():
    global screen
    if 995 < mouseX < 1245 and 635 < mouseY < 685:
        screen = 'playerScherm'
    
    elif 995 < mouseX < 1245 and 635 < mouseY < 685:
        screen = 'Startscherm'
