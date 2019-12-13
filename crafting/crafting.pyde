
def setup():
    fullScreen()

    
def draw():
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
    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
