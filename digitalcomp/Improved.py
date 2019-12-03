def setup():
    global font, diceRoll, d, flowChart1
    import random
    from random import randint
    fullScreen()
    size(800, 800)
    font = loadFont("font.vlw")
    textFont(font, 48)
    background(0)
    diceMin = 1
    diceMax = 6
    diceRoll = randint(1,6)
    d = 0
    state = homescreen
def draw():
    global randint, d, flowChart1, combat
    
    
    #displays the text on screen
    
    text("Eye of The Beholder\n\n", 50, 50)
    text("Encounter rolls\nInventory\nCombat\nRoll Dice", 50, 150)
    noFill()
    stroke(255)
    
    #draws buttons and makes them funtional including changing colour
    
    if (373 >= mouseX >= 48) and (160 >= mouseY >= 110):
        stroke(255,0,0)
        if mousePressed and (d == 0):
            # if clicked draws flowchart for area's
            d = d - 1
            clear()
            stroke(0)
            state = flowChart1
            
    if state == flowChart1:
        text("Area1\nArea2\nArea3\nArea4\nArea5", 400, 150)
        if (630 >= mouseX >= 380)and (215 >= mouseY >= 165):
            stroke(255,0,0)
            if mousePressed and (d == 0):
                stroke(0)
                d = d - 1
        stroke(255)
        rect(380, 110, 250, 50)
        rect(380, 165, 250, 50)
        rect(380, 220, 250, 50)
        rect(380, 275, 250, 50)
        rect(380, 330, 250, 50)        
    rect(48, 110, 325, 50)
    stroke(255)
    if (373 >= mouseX >= 48) and (215 >= mouseY >= 165):
        stroke(255,0,0)
        if mousePressed:
            stroke(0)
    rect(48, 165, 325, 50)
    stroke(255)
    if (373 >= mouseX >= 48) and (270 >= mouseY >= 220):
        stroke(255, 0, 0)
        if mousePressed:
            stroke(0)
            clear()
            Module = True
            stroke(255)
            combat()
    rect(48, 220, 325, 50)
    stroke(255)
    if (373 >= mouseX >= 48) and (325 >= mouseY >= 275):
        stroke(255, 0, 0)
        diceRoll = ""
        if (mousePressed and (d == 0)):
            #if clicked rolls dice and displays it on screen
            stroke(0)
            clear()
            d = d - 1
            diceRoll = random.randint(1,6)
            text(str(diceRoll), 380, 330)
            flowChart1 = False
    rect(48, 275, 325, 50)
    stroke(255)

def mouseReleased():
    global d
    d = 0
