tekst = ""
monster = ""
dice = int(random(1,6))

def setup():
    fullScreen()

    
def draw():
    global dice
    background(0,0,0)
    textSize(60)
    textAlign(CENTER)
    text("Monster name", width /2, height/ 5)
    textSize(25)
    textAlign(LEFT)
    text(tekst,  width / 2 - 40, height/ 2)
    if monster == "wolf":
        if dice == 1 or dice == 3 or dice == 4:
            textAlign(CENTER)
            text("Wolf Skin", width /2, height - 200)
        elif dice == 2 or dice == 5:
            textAlign(CENTER)
            text("Nothing", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Wolf Skin x2", width /2, height - 200)
    if monster == "bear":
        if dice == 1:
            textAlign(CENTER)
            text("Bear Skin", width /2, height - 200)
        elif dice == 2 or dice == 5:
            textAlign(CENTER)
            text("Nothing", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Bear Skin x2", width /2, height - 200)
    if monster == "skeleton":
        if dice == 1 or dice == 6:
            textAlign(CENTER)
            text("Iron Chunk", width /2, height - 200)
        elif dice == 2 or dice == 3:
            textAlign(CENTER)
            text("Wooden Stick", width /2, height - 200)
        elif dice == 4:
            textAlign(CENTER)
            text("Iron Chunk x2", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Soul of the Dead", width /2, height - 200)
    if monster == "treant":
        if dice == 3 or dice == 5:
            textAlign(CENTER)
            text("Wooden Chunk x3", width /2, height - 200)
        elif dice == 4 or dice == 6:
            textAlign(CENTER)
            text("Wooden Stick x3", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Wooden Stick", width /2, height - 200)
    if monster == "arcane wolf":
        if dice == 1 or dice == 3 or dice == 4:
            textAlign(CENTER)
            text("Enchanted Wolf Skin", width /2, height - 200)
        elif dice == 2 or dice == 5:
            textAlign(CENTER)
            text("Mana Essence", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Enchanted Wolf Skin x2", width /2, height - 200)
    if monster == "fairy":
        if dice == 1 or dice == 5 or dice == 4 or dice == 6:
            textAlign(CENTER)
            text("Mana Essence", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Mana Essence x2", width /2, height - 200)
    if monster == "mana golem":
        if dice == 1 or dice == 2:
            textAlign(CENTER)
            text("Mana Essence x2", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Obsidian", width /2, height - 200)
    if monster == "skeleton mage":
        if dice == 3 or dice == 4:
            textAlign(CENTER)
            text("Soulf od the Dead", width /2, height - 200)
        elif dice == 2:
            textAlign(CENTER)
            text("Mana Essence", width /2, height - 200)
        elif dice == 5 or dice == 6:
            textAlign(CENTER)
            text("Soul of the Dead x2", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Mana Essence x2", width /2, height - 200)
    if monster == "void spawn":
        if dice == 2 or dice == 4:
            textAlign(CENTER)
            text("Void Energy x2", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Void Energy", width /2, height - 200)
    if monster == "ghost":
        if dice == 1 or dice == 3 or dice == 6:
            textAlign(CENTER)
            text("Soul of the Dead", width /2, height - 200)
        elif dice == 2 or dice == 4:
            textAlign(CENTER)
            text("Soul of the Dead x3", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Wolf Skin x2", width /2, height - 200)
    if monster == "zombie":
        if dice in range(1,6 +1):
            textAlign(CENTER)
            text("Soul of the Dead x2", width /2, height - 200)
    if monster == "haunter":
        if dice == 3 or dice == 6 or dice == 1:
            textAlign(CENTER)
            text("Soul of the Dead", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Haunted Spirit", width /2, height - 200)
    if monster == "haunted tree":
        if dice == 1 or dice == 6:
            textAlign(CENTER)
            text("Haunted Spirit", width /2, height - 200)
        elif dice == 3:
            textAlign(CENTER)
            text("Cursed Wood x2", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Cursed Wood", width /2, height - 200)
    if monster == "golden scarab":
        if dice == 3 or dice == 5:
            textAlign(CENTER)
            text("Gold Ingot x2", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Gold Ingot", width /2, height - 200)
    if monster == "ancient skeleton":
        if dice == 2 or dice == 4:
            textAlign(CENTER)
            text("Soul of the Dead x5", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Gold Ingot", width /2, height - 200)
    if monster == "giant scorpion":
        if dice in range(1, 6+1):
            textAlign(CENTER)
            text("Scorpion Poison", width /2, height - 200)

def keyPressed():
    global tekst, monster
    if (key == ENTER):
        monster = tekst
        tekst = ""
        print(monster)
    
    else:
        tekst = tekst + key





    
        
