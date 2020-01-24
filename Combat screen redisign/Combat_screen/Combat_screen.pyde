def setup():
    global Lillie, monsterTest, psn
    fullScreen()
    background(0)
    Lillie = loadImage('Lillie of the Valley.png')
    monsterTest = loadImage('fairy.png')
    psn = loadImage('psn.png')
    
def draw():
    global Lillie, monsterTest, psn
    image(Lillie, 150, 600, width // 6, height // 3)
    textSize(50)
    text('HP: 100', 500, 650)
    text('Block: 20', 500, 750)
    text('Status:', 750, 650)
    image(psn, 920, 620)
    
    image(monsterTest, 1500, 100, width // 6, height // 3)
    text('HP: 100', 900, 150)
    text('Block: 20', 900, 250)
    text('status:', 1150, 150)
    
    
    text('Choose attack', 500, 1000)
    noFill()
    stroke(255)
    rect(495, 950, 350, 60)
