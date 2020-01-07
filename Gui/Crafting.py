import inventory

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
    inventory.setup()
    global basic_Spear, comet_Spear, doom_Spear, halberd, leather, chain, black_armour, molten_armour, platinum_armour, basic_sword, arcade_sword,obsidian_sword, dead_sword, phoenix_sword, heaven, wooden_shield, iron_shield, null_shield, gold_shield, war_god, basic_dagger, enchanted_dagger, daggerA, Iron_Chunk, Wooden_Stick
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
    global screen, basic_Spear, comet_Spear, doom_Spear, halberd, leather, chain, black_armour, molten_armour, platinum_armour, basic_sword, arcade_sword,obsidian_sword, dead_sword, phoenix_sword, heaven, wooden_shield, iron_shield, null_shield, gold_shield, war_god, basic_dagger, enchanted_dagger, daggerA, tekst, crafted_item, crafted_item2, crafted_item3, crafted_item4, crafted_item5
    #Als screen 0 is wordt de crafting pagina getekent
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
        rect(200, 700, 400, 200)
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
        fill(0)
        rect(1600, 100, 150, 60)
        textSize(30)
        textAlign(CENTER)
        fill(240)
        text("inventory", 1675, 140)
        text("Go back",245,140)
        
        if isMouseWithinSpace(1300, 700, 400, 200):
            noFill()
            rect( 200,  350, 400, 200)
            noFill()
            rect( 200,  700, 400, 200)
            noFill()
            rect( 1300, 350, 400, 200)
            fill(200)
            rect( 1300, 700, 400, 200)
            fill(240)
            text("Spear", 1500, 810)
            noFill()
            rect(1600, 100, 150, 60)
            
        if isMouseWithinSpace(200,  350, 400, 200):
            fill(200)
            rect( 200,  350, 400, 200)
            fill(240)
            text("Sword",400, 460)
            noFill()
            rect(200,  700, 400, 200)
            noFill()
            rect( 1300, 350, 400, 200)
            noFill()
            rect( 1300, 700, 400, 200)
            noFill()
            rect(1600, 100, 150, 60)
            
        if isMouseWithinSpace(200,  700, 400, 200):
            noFill()
            rect( 200,  350, 400, 200)
            fill(200)
            rect( 200,  700, 400, 200)
            fill(240)
            text("Armour", 400, 810)
            noFill()
            rect( 1300, 350, 400, 200)
            noFill()
            rect( 1300, 700, 400, 200)
            noFill()
            rect(1600, 100, 150, 60)
            
        if isMouseWithinSpace(1300, 350, 400, 200):
            noFill()
            rect( 200,  350, 400, 200)
            noFill()
            rect( 200,  700, 400, 200)
            fill(200)
            rect( 1300, 350, 400, 200)
            fill(240)
            text("Shield", 1500, 460)
            noFill()
            rect( 1300, 700, 400, 200)
            noFill()
            rect(1600, 100, 150, 60)
    
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
        image(basic_Spear, 200, 425)
        #(390, 240, 280, 380)
        image(comet_Spear, 500, 425)
        #(690, 240, 280, 380)
        image(doom_Spear, 800, 425)
        #(990, 240, 280, 380)
        image(halberd, 1100, 425)
        
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
        
        image(basic_sword, 200, 425)
        image(arcade_sword, 500, 425)
        image(obsidian_sword, 800, 425)
        image(dead_sword, 1100, 425)
        image(phoenix_sword, 1400, 425)
        image(heaven, 1700, 425)

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
        
        image(leather, 200, 425)
        image(chain, 500, 425)
        image(black_armour, 800, 425)
        image(molten_armour, 1100, 425)
        image(platinum_armour, 1400, 425)
        
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
        
        image(wooden_shield, 200, 425)
        image(iron_shield, 500, 425)
        image(null_shield, 800, 425)
        image(gold_shield, 1100, 425)
        image(war_god, 1400, 425)
        
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
        
        image(basic_dagger, 200, 425)
        image(enchanted_dagger, 500, 425)
        image(daggerA, 800, 425)
        
    if screen == "inventory":
        background(0,0,0)
        font = createFont("Georgia", 54)
        textFont(font)
        textAlign(CENTER, TOP)
        text("Inventory", 980, 100)
        stroke(240)
        line(0, 210, 2000, 210)        
        inventory.draw()

    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
    
#def increaseCurrentNumber():
    #global currentNumber
    #if currentNumber < 1000:
       #currentNumber = currentNumber + 1

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
        if isMouseWithinSpace(1600, 100, 150, 60):
            screen = "inventory"
        
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
                if inventory.Iron_Chunk < 2 and inventory.Wooden_Stick < 5:
                    crafted_item = "you don't have enough materials" 
                else:
                    crafted_item = "You have crafted basic spear"
            else:
                crafted_item = ""  
    if spear_item == 2:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Basic_Spear < 1 and inventory.Mana_Essence < 10:
                    crafted_item = "you don't have enough materials"
                else:
                    crafted_item = "You have crafted comet spear"
            else:
                crafted_item = ""   
    if spear_item == 3:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Comet_Spear < 1 and inventory.Soul_Dead < 3 and inventory.Wooden_Stick < 3:
                    crafted_item = "you don't have enough materials"
                else: 
                    crafted_item = "You have crafted necrotic spear of doom"  
            else:
                crafted_item = ""      
    if spear_item == 4:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Spear_Doom < 1 and inventory.Fire_Essence < 5:
                    crafted_item = "you don't have enough materials"
                else:
                    crafted_item = "You have crafted halberd of the fire god"
            else:
                crafted_item = ""
                
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
                if inventory.Iron_Chunk < 2 and inventory.Wooden_Stick < 1:
                    crafted_item4 = "you don't have enough materials"
                else:
                    crafted_item4 = "You have crafted basic sword"   
            else:
                crafted_item4 = ""
    if sword_item == 2:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Basic_Sword < 1 and inventory.Mana_Essence < 10:
                    crafted_item4 = "you don't have enough materials"
                else:
                    crafted_item4 = "You have crafted arcane sword"     
            else:
                crafted_item4 = ""   
    if sword_item == 3:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Basic_Sword < 1 and inventory.Obsidian < 2:
                    crafted_item4 = "you don't have enough materials"
                else:
                    crafted_item4 = "You have crafted obsidian sword"
            else:
                crafted_item4 = ""       
    if sword_item == 4:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Arcane_Sword < 1 and inventory.Soul_Dead < 5:
                    crafted_item4 = "you don't have enough materials"
                else:
                    crafted_item4 = "You have crafted sword of the dead"
            else:
                crafted_item4 = ""
    if sword_item == 5:
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Lost_Blade < 1 and inventory.Fire_Essence < 5:
                    crafted_item4 = "you don't have enough materials"
                else:
                    crafted_item4 = "You have crafted sword of phoenix"
            else:
                crafted_item4 = ""
    if sword_item == 6:
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Sword_Phoenix < 1 and inventory.Void_Essence < 5:
                    crafted_item4 = "you don't have enough materials"
                else:
                    crafted_item4 = "You have crafted heaven's wrath'"
            else:
                crafted_item4 = ""
            
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
                if inventory.Wolf_Skin < 5 or inventory.Bear_Skin < 5:
                    crafted_item3 = "you don't have enough materials"
                else:
                    crafted_item3 = "You have crafted leather armour"
            else:
                crafted_item3 = ""         
    if armour_item == 2:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Iron_Chunk < 10:
                    crafted_item3 = "you don't have enough materials"
                else:
                    crafted_item3 = "You have crafted chain armour"   
            else:
                crafted_item3 = ""     
    if armour_item == 3:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Chain_Armour < 1 and inventory.Soul_Dead < 5 and inventory.Obsidian < 2:
                    crafted_item3 = "you don't have enough materials"
                else:
                    crafted_item3 = "You have crafted black armour"  
            else:
                crafted_item3 = ""     
    if armour_item == 4:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Black_Armour < 1 and inventory.Fire_Essence < 5:
                    crafted_item3 = "you don't have enough materials"
                else:
                    crafted_item3 = "You have crafted molten armour"
            else:
                crafted_item3 = ""
    if armour_item == 5:
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Molten_Armour < 1 and inventory.Void_Essence < 10:
                    crafted_item3 = "you don't have enough materials"
                else:
                    crafted_item3 = "You have crafted amadantium plate"
            else:
                crafted_item3 = ""
            
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
                if inventory.Wooden_Chunk < 5 and inventory.Wooden_Stick < 2:
                    crafted_item2 = "you don't have enough materials"
                else:
                    crafted_item2 = "You have crafted wooden shield"    
            else:
                crafted_item2 = ""        
    if shield_item == 2:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Wooden_Shield < 1 and inventory.Iron_Chunk < 5:
                    crafted_item2 = "you don't have enough materials"
                else:
                    crafted_item2 = "You have crafted iron shield" 
            else:
                crafted_item2 = ""       
    if shield_item == 3:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Iron_Shield < 1 and inventory.Mana_Essence < 10:
                    crafted_item2= "you don't have enough materials"
                else:
                    crafted_item2 = "You have crafted null shield" 
            else:
                crafted_item2 = ""        
    if shield_item == 4:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Iron_Shield < 1 and inventory.Null_Shield < 1 and inventory.Gold_Ingot < 3:
                    crafted_item2 = "you don't have enough materials"
                else:
                    crafted_item2 = "You have crafted gold shield"
            else:
                crafted_item2 = ""
    if shield_item == 5:
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Gold_Shield < 1 and inventory.Void_Essence < 10:
                    crafted_item2 = "you don't have enough materials"
                else:
                    crafted_item2 = "You have crafted war god's aegis"
            else:
                crafted_item2 = ""
        
    if screen == 5:
        if isMouseWithinSpace(150, 100, 150, 60):
            screen = 1
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
                if inventory.Iron_Chunk < 1 and inventory.Wooden_Stick < 1:
                    crafted_item5 = "you don't have enough materials"
                else:
                    crafted_item5 = "You have crafted basic dagger"   
            else:
                crafted_item5 = ""         
    if dagger_item == 2:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Basic_Dagger < 1 and inventory.Mana_Essence < 3:
                    crafted_item5 = "you don't have enough materials"
                else:
                    crafted_item5 = "You have crafted enchanted dagger"    
            else:
                crafted_item5 = ""    
    if dagger_item == 3:    
        if tekst == "Craft":
            if isMouseWithinSpace(150, 850, 150, 60):
                if inventory.Enchanted_Dagger < 1 and inventory.Scorpion_Poison < 3:
                    crafted_item5 = "you don't have enough materials"
                else:
                    crafted_item5 = "You have crafted dagger of affliction"
            else:
                crafted_item5 = ""
