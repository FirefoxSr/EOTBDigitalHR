import cards


def setup():
    global Lillie, monsterTest, psn, screen
    fullScreen()
    background(0)
    Lillie = loadImage('Lillie of the Valley.png')
    monsterTest = loadImage('fairy.png')
    psn = loadImage('psn.png')
    screen = 'combat'
def draw():
    global Lillie, monsterTest, psn, screen
    image(Lillie, 150, 600, width // 6, height // 3)
    textSize(50)
    text('HP: 100', 500, 650)
    text('Block: 20', 500, 750)
    text('Status:', 750, 650)
    text('energy:', 500, 850)
    image(psn, 920, 620)
    
    image(monsterTest, 1500, 100, width // 6, height // 3)
    text('HP: 100', 900, 150)
    text('Block: 20', 900, 250)
    text('status:', 1150, 150)
    text('energy:', 900, 350)
    
    
    text('Choose attack', 500, 1000)
    noFill()
    stroke(255)
    rect(495, 950, 350, 60)
    
    if screen == 'cards':
        cards.setup()
        cards.draw()
    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mouseClicked():
    global screen
    if isMouseWithinSpace(495, 950, 650, 60):
        screen = 'cards'
        
