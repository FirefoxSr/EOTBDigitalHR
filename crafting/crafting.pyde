screen = 0
def setup():
    fullScreen()
    global basic_Spear, comet_Spear, doom_Spear, halberd, leather, chain, black_armour, molten_armour, platinum_armour, basic_sword, arcade_sword,obsidian_sword, dead_sword, phoenix_sword, heaven
    basic_Spear = loadImage("basicSpear1.png")
    comet_Spear = loadImage("comet.png")
    doom_Spear = loadImage("doom.png")
    halberd = loadImage("halberd.png")
    leather = loadImage("leather.png")
    chain = loadImage("chain.png")
    black_armour = loadImage("blackAmour.png")
    molten_armour = loadImage("molten.png")
    platinum_armour = loadImage("platinum.png")
    basic_sword = loadImage("basicSword.png")
    arcade_sword = loadImage("arcadeSword.png")
    obsidian_sword = loadImage("obsidianSword.png")
    dead_sword = loadImage("deadSword.png")
    phoenix_sword = loadImage("phoenixSword.png")
    heaven = loadImage("heaven.png")

        
def draw():
    global basic_Spear, comet_Spear, doom_Spear, halberd, leather, chain, black_armour, molten_armour, platinum_armour, basic_sword, arcade_sword,obsidian_sword, dead_sword, phoenix_sword, heaven
    if screen == 0:
        background(0,0,0)
        textSize(52)
        textAlign(CENTER)
        fill(240)
        text("Crafting", width /2, height /8)
        stroke(240)
        line(0, 210, 2000, 210)
        
        stroke(240)
        fill(0)
        rect( 200,  350, 400, 200)
        textSize(30)
        fill(240)
        text("Sword",400, 460)
        fill(0)
        rect( 200,  700, 400, 200)
        fill(240)
        text("Armour", 400, 810)
        fill(0)
        rect( 1300, 350, 400, 200)
        fill(240)
        text("Shield", 1500, 460)
        fill(0)
        rect( 1300, 700, 400, 200)
        fill(240)
        text("Spear", 1500, 810)
    
    if screen == 4:
        background(0,0,0)
        textSize(52)
        textAlign(CENTER)
        fill(240)
        text("Spear", width /2, height /8)
        stroke(240)
        line(0, 210, 2000, 210)
        fill(0)
        rect(150, 100, 150, 60)
        textSize(30)
        textAlign(CENTER)
        fill(240)
        text("Back", 225, 140)
        
        image(basic_Spear, 100, 250)
        image(comet_Spear, 400, 250)
        image(doom_Spear, 700, 250)
        image(halberd, 1000, 250)
        
    if screen == 1:
        background(0,0,0)
        textSize(52)
        textAlign(CENTER)
        fill(240)
        text("Sword", width /2, height /8)
        stroke(240)
        line(0, 210, 2000, 210)
        fill(0)
        rect(150, 100, 150, 60)
        textSize(30)
        textAlign(CENTER)
        fill(240)
        text("Back", 225, 140)
        
        image(basic_sword, 100, 250)
        image(arcade_sword, 400, 250)
        image(obsidian_sword, 700, 250)
        image(dead_sword, 1000, 250)
        image(phoenix_sword, 1300, 250)
        image(heaven, 1600, 250)

    if screen == 2:
        background(0,0,0)
        textSize(52)
        textAlign(CENTER)
        fill(240)
        text("Armour", width /2, height /8)
        stroke(240)
        line(0, 210, 2000, 210)
        fill(0)
        rect(150, 100, 150, 60)
        textSize(30)
        textAlign(CENTER)
        fill(240)
        text("Back", 225, 140)
        
        image(leather, 100, 250)
        image(chain, 400, 250)
        image(black_armour, 700, 250)
        image(molten_armour, 1000, 250)
        image(platinum_armour, 1300, 250)
        
    if screen == 3:
        background(0,0,0)
        textSize(52)
        textAlign(CENTER)
        fill(240)
        text("Shield", width /2, height /8)
        stroke(240)
        line(0, 210, 2000, 210)
        fill(0)
        rect(150, 100, 150, 60)
        textSize(30)
        textAlign(CENTER)
        fill(240)
        text("Back", 225, 140)
    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mousePressed():
    global screen
    if screen == 0:
        if isMouseWithinSpace(1300, 700, 400, 200):
            screen = 4
        if isMouseWithinSpace(200,  350, 400, 200):
            screen = 1  
        if isMouseWithinSpace(200,  700, 400, 200):
            screen = 2
        if isMouseWithinSpace(1300, 350, 400, 200):
            screen = 3
        
    if screen == 4:
        if isMouseWithinSpace(150, 100, 150, 60):
            screen = 0
    if screen == 1:
        if isMouseWithinSpace(150, 100, 150, 60):
            screen = 0
    if screen == 2:
        if isMouseWithinSpace(150, 100, 150, 60):
            screen = 0
    if screen == 3:
        if isMouseWithinSpace(150, 100, 150, 60):
            screen = 0
