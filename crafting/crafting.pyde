screen = 0
tekst = ""
crafted_item = ""
crafted_item2 = ""
crafted_item3 = ""
crafted_item4 = ""
crafted_item5 = ""
spear_item = 0
shield_item = 0
armour_item = 0
sword_item = 0
dagger_item = 0
def setup():
    fullScreen()
    global basic_Spear, comet_Spear, doom_Spear, halberd, leather, chain, black_armour, molten_armour, platinum_armour, basic_sword, arcade_sword,obsidian_sword, dead_sword, phoenix_sword, heaven, wooden_shield, iron_shield, null_shield, gold_shield, war_god, basic_dagger, enchanted_dagger, daggerA
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
    wooden_shield = loadImage("woodenShield.png")
    iron_shield = loadImage("ironShield.png")
    null_shield = loadImage("nullShield.png")
    gold_shield = loadImage("goldShield.png")
    war_god = loadImage("wargod.png")
    basic_dagger = loadImage("basicDagger.png")
    enchanted_dagger = loadImage("enchantedDagger.png")
    daggerA = loadImage("daggerA.png")
                            

        
def draw():
    global basic_Spear, comet_Spear, doom_Spear, halberd, leather, chain, black_armour, molten_armour, platinum_armour, basic_sword, arcade_sword,obsidian_sword, dead_sword, phoenix_sword, heaven, wooden_shield, iron_shield, null_shield, gold_shield, war_god, basic_dagger, enchanted_dagger, daggerA, tekst, crafted_item, crafted_item2, crafted_item3, crafted_item4, crafted_item5
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
        #rect(150, 850, 150, 60)
        fill(240)
        textSize(52)
        text(tekst, 225, 900)
        fill(240)
        textAlign(LEFT)
        text(crafted_item, 800, 900)

        #(90, 240, 280, 380)
        image(basic_Spear, 100, 250)
        #(390, 240, 280, 380)
        image(comet_Spear, 400, 250)
        #(690, 240, 280, 380)
        image(doom_Spear, 700, 250)
        #(990, 240, 280, 380)
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
        fill(240)
        textSize(52)
        text(tekst, 225, 900)
        fill(240)
        textAlign(LEFT)
        text(crafted_item4, 800, 900)
        fill(0)
        rect(1600, 100, 150, 60)
        textSize(30)
        textAlign(CENTER)
        fill(240)
        text("Dagger", 1675, 140)
        
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
        fill(240)
        textSize(52)
        text(tekst, 225, 900)
        fill(240)
        textAlign(LEFT)
        text(crafted_item3, 800, 900)
        
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
        fill(240)
        textSize(52)
        text(tekst, 225, 900)
        fill(240)
        textAlign(LEFT)
        text(crafted_item2, 800, 900)
        
        image(wooden_shield, 100, 250)
        image(iron_shield, 400, 250)
        image(null_shield, 700, 250)
        image(gold_shield, 1000, 250)
        image(war_god, 1300, 250)
        
    if screen == 5:
        background(0,0,0)
        textSize(52)
        textAlign(CENTER)
        fill(240)
        text("Dagger", width /2, height /8)
        stroke(240)
        line(0, 210, 2000, 210)
        fill(0)
        rect(150, 100, 150, 60)
        textSize(30)
        textAlign(CENTER)
        fill(240)
        text("Back", 225, 140)
        fill(240)
        textSize(52)
        text(tekst, 225, 900)
        fill(240)
        textAlign(LEFT)
        text(crafted_item5, 800, 900)
        
        image(basic_dagger, 100, 250)
        image(enchanted_dagger, 400, 250)
        image(daggerA, 700, 250)
    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mousePressed():
    global screen, tekst, crafted_item, spear_item, shield_item, crafted_item2, armour_item, crafted_item3, crafted_item4, sword_item, crafted_item5, dagger_item
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
        if isMouseWithinSpace(90, 240, 280, 380):
            tekst = "Craft"
            spear_item = 1
        elif isMouseWithinSpace(390, 240, 280, 380):
            tekst = "Craft"
            spear_item = 2
        elif isMouseWithinSpace(690, 240, 280, 380):
            tekst = "Craft"
            spear_item = 3
        elif isMouseWithinSpace(990, 240, 280, 380):
            tekst = "Craft"
            spear_item = 4
    if spear_item == 1:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item = "You have crafted basic spear"            
    if spear_item == 2:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item = "You have crafted comet spear"        
    if spear_item == 3:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item = "You have crafted necrotic spear of doom"        
    if spear_item == 4:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item = "You have crafted halberd of the fire god"
                
    if screen == 1:
        if isMouseWithinSpace(150, 100, 150, 60):
            screen = 0
        elif isMouseWithinSpace(1600, 100, 150, 60):
            screen = 5
        if isMouseWithinSpace(90, 240, 280, 380):
            tekst = "Craft"
            sword_item = 1
        elif isMouseWithinSpace(390, 240, 280, 380):
            tekst = "Craft"
            sword_item = 2
        elif isMouseWithinSpace(690, 240, 280, 380):
            tekst = "Craft"
            sword_item = 3
        elif isMouseWithinSpace(990, 240, 280, 380):
            tekst = "Craft"
            sword_item = 4
        elif isMouseWithinSpace(1290, 240, 280, 380):
            tekst = "Craft"
            sword_item = 5
        elif isMouseWithinSpace(1590, 240, 280, 380):
            tekst = "Craft"
            sword_item = 6
    if sword_item == 1:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item4 = "You have crafted basic sword"            
    if sword_item == 2:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item4 = "You have crafted arcane sword"        
    if sword_item == 3:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item4 = "You have crafted obsidian sword"        
    if sword_item == 4:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item4 = "You have crafted sword of the dead"
    if sword_item == 5:
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item4 = "You have crafted sword of phoenix"
    if sword_item == 6:
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item4 = "You have crafted heaven's wrath'"
            
    if screen == 2:
        if isMouseWithinSpace(150, 100, 150, 60):
            screen = 0
        if isMouseWithinSpace(90, 240, 280, 380):
            tekst = "Craft"
            armour_item = 1
        elif isMouseWithinSpace(390, 240, 280, 380):
            tekst = "Craft"
            armour_item = 2
        elif isMouseWithinSpace(690, 240, 280, 380):
            tekst = "Craft"
            armour_item = 3
        elif isMouseWithinSpace(990, 240, 280, 380):
            tekst = "Craft"
            armour_item = 4
        elif isMouseWithinSpace(1290, 240, 280, 380):
            tekst = "Craft"
            armour_item = 5
    if armour_item == 1:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item3 = "You have crafted leather armour"            
    if armour_item == 2:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item3 = "You have crafted chain armour"        
    if armour_item == 3:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item3 = "You have crafted black armour"        
    if armour_item == 4:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item3 = "You have crafted molten armour"
    if armour_item == 5:
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item3 = "You have crafted amadantium plate"
            
    if screen == 3:
        if isMouseWithinSpace(150, 100, 150, 60):
            screen = 0
        if isMouseWithinSpace(90, 240, 280, 380):
            tekst = "Craft"
            shield_item = 1
        elif isMouseWithinSpace(390, 240, 280, 380):
            tekst = "Craft"
            shield_item = 2
        elif isMouseWithinSpace(690, 240, 280, 380):
            tekst = "Craft"
            shield_item = 3
        elif isMouseWithinSpace(990, 240, 280, 380):
            tekst = "Craft"
            shield_item = 4
        elif isMouseWithinSpace(1290, 240, 280, 380):
            tekst = "Craft"
            shield_item = 5
    if shield_item == 1:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item2 = "You have crafted wooden shield"            
    if shield_item == 2:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item2 = "You have crafted iron shield"        
    if shield_item == 3:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item2 = "You have crafted null shield"        
    if shield_item == 4:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item2 = "You have crafted gold shield"
    if shield_item == 5:
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item2 = "You have crafted war god's aegis"
        
    if screen == 5:
        if isMouseWithinSpace(150, 100, 150, 60):
            screen = 1
        if isMouseWithinSpace(150, 100, 150, 60):
            screen = 0
        if isMouseWithinSpace(90, 240, 280, 380):
            tekst = "Craft"
            dagger_item = 1
        elif isMouseWithinSpace(390, 240, 280, 380):
            tekst = "Craft"
            dagger_item = 2
        elif isMouseWithinSpace(690, 240, 280, 380):
            tekst = "Craft"
            dagger_item = 3
    if dagger_item == 1:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item5 = "You have crafted basic dagger"            
    if dagger_item == 2:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item5 = "You have crafted enchanted dagger"        
    if dagger_item == 3:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                crafted_item5 = "You have crafted dagger of affliction"
