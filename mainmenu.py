def setup():
    global font, diceRoll, state, mainMenu, combat, encounters
    size(800, 800)
    textFont(font, 48)
    background(0)
    diceMin = 1
    diceMax = 6
    diceRoll = randint(1,6)
def draw():
    text("Eye of The Beholder\n\n", 50, 50)
    text("Encounter rolls\nInventory\nCombat", 50, 150)
    noFill()
    stroke(255)
    #button functionality
    if (373 >= mouseX >= 48) and (160 >= mouseY >= 110):
        stroke(255,0,0)
        if mousePressed:
            stroke(0)
            text("Area1\nArea2\nArea3\nArea4\nArea5",400, 150) 
            stroke(255)
            if (630 >= mouseX >= 380) and (215 >= mouseY >= 165):
                stroke(255,0,0)
                if mousePressed:
                    stroke(0)
            stroke(255)
            #draws boxes around the area buttons
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
            state = combat
    rect(48, 220, 325, 50)
