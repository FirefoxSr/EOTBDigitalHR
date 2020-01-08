import inventory
import Map
import playerTurns
import inventory2
import Combat

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
    #Load items images
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
   
     #If screen == 0 it will draw the Crafting page
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
    
    #This will fill the rectangle with a colour to let the player know which button he/she has selected
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
            
    #if the screen == 4 it will draw the Crafting for the spear page
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

        #This draws the images of the spear items
        image(basic_Spear, 100, 250)
        image(comet_Spear, 400, 250)
        image(doom_Spear, 700, 250)
        image(halberd, 1000, 250)
     
    #If screen == 1 it will draw the Crafting for the sword page
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
        
        #This draws the images of sword items
        image(basic_sword, 100, 250)
        image(arcade_sword, 400, 250)
        image(obsidian_sword, 700, 250)
        image(dead_sword, 1000, 250)
        image(phoenix_sword, 1300, 250)
        image(heaven, 1600, 250)

    #if screen == 0 it will draw the Crafting for the armour page
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
        
        #This will draw the images of armour items 
        image(leather, 100, 250)
        image(chain, 400, 250)
        image(black_armour, 700, 250)
        image(molten_armour, 1000, 250)
        image(platinum_armour, 1300, 250)
        
    #if screen == 3 it will draw the Crafting for the shield page
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
        
        #This will draw the images of shield items
        image(wooden_shield, 100, 250)
        image(iron_shield, 400, 250)
        image(null_shield, 700, 250)
        image(gold_shield, 1000, 250)
        image(war_god, 1300, 250)
        
    #if screen == 5 it will draw the Crating for the Dagger page
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
        
        #This will draw the images dagger items
        image(basic_dagger, 100, 250)
        image(enchanted_dagger, 400, 250)
        image(daggerA, 700, 250)
        
    #When it's player 1 turn it will draw the inventory for player 1 and only player 1
    if Map.currentPlayer == 1:    
        if screen == "inventory":
            background(0,0,0)
            font = createFont("Georgia", 54)
            textFont(font)
            textAlign(CENTER, TOP)
            text("Inventory", 980, 100)
            stroke(240)
            line(0, 210, 2000, 210)        
            inventory.draw()
    
    #When it's player 2 turn it will draw the inventory for player 2 and only player 2
    if Map.currentPlayer == 2:    
        if screen == "inventory":
            background(0,0,0)
            font = createFont("Georgia", 54)
            textFont(font)
            textAlign(CENTER, TOP)
            text("Inventory2", 980, 100)
            stroke(240)
            line(0, 210, 2000, 210)        
            inventory2.draw()

    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mousePressed():
    global screen, tekst, crafted_item, spear_item, shield_item, crafted_item2, armour_item, crafted_item3, crafted_item4, sword_item, crafted_item5, dagger_item
    
    #Player 1 turn
    if Map.currentPlayer == 1:
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
        
        #This will select an item in the spear page
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

# if the selected item is selected it will look in the inventory to see if you have enough materials to craft the item
# if you have enough material it will craft the item and take the materials from the inventory
        if spear_item == 1:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Iron_Chunk < 2 and inventory.Wooden_Stick < 5:
                        crafted_item = "you don't have enough materials" 
                    else:
                        crafted_item = "You have crafted basic spear"
                        inventory.Iron_Chunk = inventory.Iron_Chunk - 2
                        inventory.Wooden_Stick = inventory.Wooden_Stick - 5
                        Combat.piercing = Combat.piercing + 4
                else:
                    crafted_item = ""  
                    
        if spear_item == 2:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Basic_Spear < 1 and inventory.Mana_Essence < 10:
                        crafted_item = "you don't have enough materials"
                    else:
                        crafted_item = "You have crafted comet spear"
                        inventory.Basic_Spear = inventory.Basic_Spear - 1
                        inventory.Mana_Essence = inventory.Mana_Essence - 10
                        Combat.piercing = Combat.piercing + 10
                else:
                    crafted_item = ""   
                    
        if spear_item == 3:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Comet_Spear < 1 and inventory.Soul_Dead < 3 and inventory.Wooden_Stick < 3:
                        crafted_item = "you don't have enough materials"
                    else: 
                        crafted_item = "You have crafted necrotic spear of doom" 
                        inventory.Comet_Spear = inventory.Comet_Spear - 1
                        inventory.Soul_Dead = inventory.Soul_Dead - 3
                        inventory.Wooden_Stick = inventory.Wooden_Stick - 3 
                        Combat.piercing = Combat.piercing + 18
                else:
                    crafted_item = ""   
                       
        if spear_item == 4:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Spear_Doom < 1 and inventory.Fire_Essence < 5:
                        crafted_item = "you don't have enough materials"
                    else:
                        crafted_item = "You have crafted halberd of the fire god"
                        inventory.Spear_Doom = inventory.Spear_Doom - 1
                        inventory.Fire_Essence = inventory.Fire_Essence
                        Combat.fire = Combat.fire + 100
                else:
                    crafted_item = ""
                  
        #This will select an item in the sword page                      
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
                
# if the selected item is selected it will look in the inventory to see if you have enough materials to craft the item
# if you have enough material it will craft the item and take the materials from the inventory            
        if sword_item == 1:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Iron_Chunk < 2 and inventory.Wooden_Stick < 1:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted basic sword"   
                        inventory.Iron_Chunk = inventory.Iron_Chunk - 2
                        inventory.Wooden_Stick = inventory.Wooden_Stick - 1
                        Combat.damage = Combat.damage + 3
                else:
                    crafted_item4 = ""
                    
        if sword_item == 2:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Basic_Sword < 1 and inventory.Mana_Essence < 10:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted arcane sword"
                        inventory.Basic_Sword = inventory.Basic_Sword - 1
                        inventory.Mana_Essence = inventory.Mana_Essence - 10 
                        Combat.damage = Combat.damage + 8  
                else:
                    crafted_item4 = "" 
                      
        if sword_item == 3:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Basic_Sword < 1 and inventory.Obsidian < 2:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted obsidian sword"
                        inventory.Basic_Sword = inventory.Basic_Sword - 1
                        inventory.Obsidian = inventory.Obsidian - 2
                        Combat.damage = Combat.damage + 10
                else:
                    crafted_item4 = ""   
                        
        if sword_item == 4:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Arcane_Sword < 1 and inventory.Soul_Dead < 5:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted sword of the dead"
                        inventory.Arcane_Sword = inventory.Arcane_Sword - 1
                        inventory.Soul_Dead = inventory.Soul_Dead - 5
                        Combat.damage = Combat.damage + 10
                else:
                    crafted_item4 = ""
                    
        if sword_item == 5:
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Lost_Blade < 1 and inventory.Fire_Essence < 5:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted sword of phoenix"
                        inventory.Lost_Blade = inventory.Lost_Blade -1
                        inventory.Fire_Essence = inventory.Fire_Essence - 5
                        Combat.damage = Combat.damage + 70
                else:
                    crafted_item4 = ""
                    
        if sword_item == 6:
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Sword_Phoenix < 1 and inventory.Void_Essence < 5:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted heaven's wrath'"
                        inventory.Sword_Phoenix = inventory.Sword_Phoenix - 1
                        inventory.Void_Essence = inventory.Void_Essence - 5
                        Combat.damage = Combat.damage + 140
                else:
                    crafted_item4 = ""
                    
        #This will select an item in the armour page
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

# if the selected item is selected it will look in the inventory to see if you have enough materials to craft the item
# if you have enough material it will craft the item and take the materials from the inventory            
        if armour_item == 1:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Wolf_Skin < 5 or inventory.Bear_Skin < 5:
                        crafted_item3 = "you don't have enough materials"
                    else:
                        crafted_item3 = "You have crafted leather armour"
                        inventory.Wolf_Skin = inventory.Wolf_Skin - 5
                        inventory.Bear_Skin = inventory.Bear_Skin - 5
                        Combat.P_health = Combat.P_health + 15
                else:
                    crafted_item3 = ""   
                          
        if armour_item == 2:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Iron_Chunk < 10:
                        crafted_item3 = "you don't have enough materials"
                    else:
                        crafted_item3 = "You have crafted chain armour"
                        inventory.Iron_Chunk = inventory.Iron_Chunk - 10   
                        Combat.P_health = Combat.P_health + 15
                else:
                    crafted_item3 = ""     
                    
        if armour_item == 3:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Chain_Armour < 1 and inventory.Soul_Dead < 5 and inventory.Obsidian < 2:
                        crafted_item3 = "you don't have enough materials"
                    else:
                        crafted_item3 = "You have crafted black armour"  
                        inventory.Chain_Armour = inventory.Chain_Armour - 1
                        inventory.Soul_Dead = inventory.Soul_Dead - 5
                        inventory.Obsidian = inventory.Obsidian - 2
                        Combat.P_health = Combat.P_health + 50
                else:
                    crafted_item3 = ""    
                     
        if armour_item == 4:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Black_Armour < 1 and inventory.Fire_Essence < 5:
                        crafted_item3 = "you don't have enough materials"
                    else:
                        crafted_item3 = "You have crafted molten armour"
                        inventory.Black_Armour = inventory.Black_Armour - 1
                        inventory.Fire_Essence = inventory.Fire_Essence - 5
                        Combat.P_health = Combat.P_Health + 120
                        Combat.P_block = Combat.P_block +20
                else:
                    crafted_item3 = ""
                    
        if armour_item == 5:
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Molten_Armour < 1 and inventory.Void_Essence < 10:
                        crafted_item3 = "you don't have enough materials"
                    else:
                        crafted_item3 = "You have crafted amadantium plate"
                        inventory.Molten_Armour = inventory.Molten_Armour - 1
                        inventory.Mana_Essence = inventory.Mana_Essence - 10
                        Combat.P_health = Combat.P_health + 250
                else:
                    crafted_item3 = ""
      
        #This will select an item in the shield page
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

# if the selected item is selected it will look in the inventory to see if you have enough materials to craft the item
# if you have enough material it will craft the item and take the materials from the inventory                
        if shield_item == 1:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Wooden_Chunk < 5 and inventory.Wooden_Stick < 2:
                        crafted_item2 = "you don't have enough materials"
                    else:
                        crafted_item2 = "You have crafted wooden shield"
                        inventory.Wooden_Chunk = inventory.Wooden_Chunk - 5
                        inventory.Wooden_Stick = inventory.Wooden_Stick - 2    
                        Combat.P_block = Combat.P_block + 3
                else:
                    crafted_item2 = "" 
                           
        if shield_item == 2:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Wooden_Shield < 1 and inventory.Iron_Chunk < 5:
                        crafted_item2 = "you don't have enough materials"
                    else:
                        crafted_item2 = "You have crafted iron shield" 
                        inventory.Wooden_Shield = inventory.Wooden_Shield - 1
                        inventory.Iron_Chunk = inventory.IronChunk - 5
                        Combat.P_block = Combat.P_block + 5
                else:
                    crafted_item2 = "" 
                          
        if shield_item == 3:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Iron_Shield < 1 and inventory.Mana_Essence < 10:
                        crafted_item2= "you don't have enough materials"
                    else:
                        crafted_item2 = "You have crafted null shield" 
                        inventory.Iron_Shield = inventory.Iron_Shield - 1
                        inventory.Mana_Essence = inventory.Mana_Essence - 10
                        Combat.P_block = Combat.P_block + 7
                else:
                    crafted_item2 = ""
                            
        if shield_item == 4:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Iron_Shield < 1 and inventory.Null_Shield < 1 and inventory.Gold_Ingot < 3:
                        crafted_item2 = "you don't have enough materials"
                    else:
                        crafted_item2 = "You have crafted gold shield"
                        inventory.Iron_Shield = inventory.Iron_Shield - 1
                        inventory.Null_Shield = inventory.Null_Shield - 1
                        inventory.Gold_Ingot = inventory.Gold_Ingot - 3
                        Combat.P_block = Combat.P_block + 30
                else:
                    crafted_item2 = ""
                    
        if shield_item == 5:
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Gold_Shield < 1 and inventory.Void_Essence < 10:
                        crafted_item2 = "you don't have enough materials"
                    else:
                        crafted_item2 = "You have crafted war god's aegis"
                        inventory.Gold_Shield = inventory.Gold_Shield - 1
                        inventory.Void_Essence = inventory.Void_Essence - 10
                        Combat.P_block = Combat.P_block + 80
                else:
                    crafted_item2 = ""

        #This will select an item in the dagger page
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
                        inventory.Iron_Chunk = inventory.Iron_Chunk - 1
                        inventory.Wooden_Stick = inventory.Wooden_Stick  - 1 
                        Combat.P_damage = Combat.P_damage + 2 
                else:
                    crafted_item5 = ""  
                           
        if dagger_item == 2:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Basic_Dagger < 1 and inventory.Mana_Essence < 3:
                        crafted_item5 = "you don't have enough materials"
                    else:
                        crafted_item5 = "You have crafted enchanted dagger"
                        inventory.Basic_Dagger = inventory.Basic_Dagger - 1
                        inventory.Mana_Essence = inventory.Mana_Essence - 3  
                        Combat.piercing = Combat.piercing + 8
                else:
                    crafted_item5 = "" 
                       
        if dagger_item == 3:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory.Enchanted_Dagger < 1 and inventory.Scorpion_Poison < 3:
                        crafted_item5 = "you don't have enough materials"
                    else:
                        crafted_item5 = "You have crafted dagger of affliction"
                        inventory.Enchanted_Dagger = inventory.Enchanted_Dagger - 1
                        inventory.Scorpion_Poison = inventory.Scorpion_Poison - 3
                        Combat.poison = Combat.poison + 15
                else:
                        crafted_item5 = ""
    #Player 2 Turn                
    if Map.currentPlayer == 2:
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
        
        #This will select an item in the spear page
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

# if the selected item is selected it will look in the inventory to see if you have enough materials to craft the item
# if you have enough material it will craft the item and take the materials from the inventory
        if spear_item == 1:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Iron_Chunk < 2 and inventory2.Wooden_Stick < 5:
                        crafted_item = "you don't have enough materials" 
                    else:
                        crafted_item = "You have crafted basic spear"
                        inventory2.Iron_Chunk = inventory2.Iron_Chunk - 2
                        inventory2.Wooden_Stick = inventory2.Wooden_Stick - 5
                        Combat2.piercing = Combat2.piercing + 4
                else:
                    crafted_item = ""  
                    
        if spear_item == 2:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Basic_Spear < 1 and inventory2.Mana_Essence < 10:
                        crafted_item = "you don't have enough materials"
                    else:
                        crafted_item = "You have crafted comet spear"
                        inventory2.Basic_Spear = inventory2.Basic_Spear - 1
                        inventory2.Mana_Essence = inventory2.Mana_Essence - 10
                        Combat2.piercing = Combat2.piercing + 10
                else:
                    crafted_item = ""   
                    
        if spear_item == 3:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Comet_Spear < 1 and inventory2.Soul_Dead < 3 and inventory2.Wooden_Stick < 3:
                        crafted_item = "you don't have enough materials"
                    else: 
                        crafted_item = "You have crafted necrotic spear of doom" 
                        inventory2.Comet_Spear = inventory2.Comet_Spear - 1
                        inventory2.Soul_Dead = inventory2.Soul_Dead - 3
                        inventory2.Wooden_Stick = inventory2.Wooden_Stick - 3 
                        Combat2.piercing = Combat2.piercing + 18
                else:
                    crafted_item = ""   
                       
        if spear_item == 4:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Spear_Doom < 1 and inventory2.Fire_Essence < 5:
                        crafted_item = "you don't have enough materials"
                    else:
                        crafted_item = "You have crafted halberd of the fire god"
                        inventory2.Spear_Doom = inventory2.Spear_Doom - 1
                        inventory2.Fire_Essence = inventory2.Fire_Essence
                        Combat2.fire = Combat2.fire + 100
                else:
                    crafted_item = ""
                  
        #This will select an item in the sword page                      
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
                
# if the selected item is selected it will look in the inventory to see if you have enough materials to craft the item
# if you have enough material it will craft the item and take the materials from the inventory            
        if sword_item == 1:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Iron_Chunk < 2 and inventory2.Wooden_Stick < 1:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted basic sword"   
                        inventory2.Iron_Chunk = inventory2.Iron_Chunk - 2
                        inventory2.Wooden_Stick = inventory2.Wooden_Stick - 1
                        Combat2.damage = Combat2.damage + 3
                else:
                    crafted_item4 = ""
                    
        if sword_item == 2:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Basic_Sword < 1 and inventory2.Mana_Essence < 10:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted arcane sword"
                        inventory.Basic_Sword = inventory2.Basic_Sword - 1
                        inventory.Mana_Essence = inventory2.Mana_Essence - 10 
                        Combat2.damage = Combat2.damage + 8  
                else:
                    crafted_item4 = "" 
                      
        if sword_item == 3:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Basic_Sword < 1 and inventory2.Obsidian < 2:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted obsidian sword"
                        inventory2.Basic_Sword = inventory2.Basic_Sword - 1
                        inventory2.Obsidian = inventory2.Obsidian - 2
                        Combat2.damage = Combat2.damage + 10
                else:
                    crafted_item4 = ""   
                        
        if sword_item == 4:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Arcane_Sword < 1 and inventory2.Soul_Dead < 5:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted sword of the dead"
                        inventory2.Arcane_Sword = inventory2.Arcane_Sword - 1
                        inventory2.Soul_Dead = inventory2.Soul_Dead - 5
                        Combat2.damage = Combat2.damage + 10
                else:
                    crafted_item4 = ""
                    
        if sword_item == 5:
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Lost_Blade < 1 and inventory2.Fire_Essence < 5:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted sword of phoenix"
                        inventory2.Lost_Blade = inventory2.Lost_Blade -1
                        inventory2.Fire_Essence = inventory2.Fire_Essence - 5
                        Combat2.damage = Combat2.damage + 70
                else:
                    crafted_item4 = ""
                    
        if sword_item == 6:
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Sword_Phoenix < 1 and inventory2.Void_Essence < 5:
                        crafted_item4 = "you don't have enough materials"
                    else:
                        crafted_item4 = "You have crafted heaven's wrath'"
                        inventory2.Sword_Phoenix = inventory2.Sword_Phoenix - 1
                        inventory2.Void_Essence = inventory2.Void_Essence - 5
                        Combat2.damage = Combat2.damage + 140
                else:
                    crafted_item4 = ""
                    
        #This will select an item in the armour page
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

# if the selected item is selected it will look in the inventory to see if you have enough materials to craft the item
# if you have enough material it will craft the item and take the materials from the inventory            
        if armour_item == 1:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Wolf_Skin < 5 or inventory2.Bear_Skin < 5:
                        crafted_item3 = "you don't have enough materials"
                    else:
                        crafted_item3 = "You have crafted leather armour"
                        inventory2.Wolf_Skin = inventory2.Wolf_Skin - 5
                        inventory2.Bear_Skin = inventory2.Bear_Skin - 5
                        Combat2.P_health = Combat2.P_health + 15
                else:
                    crafted_item3 = ""   
                          
        if armour_item == 2:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Iron_Chunk < 10:
                        crafted_item3 = "you don't have enough materials"
                    else:
                        crafted_item3 = "You have crafted chain armour"
                        inventory2.Iron_Chunk = inventory2.Iron_Chunk - 10   
                        Combat2.P_health = Combat2.P_health + 15
                else:
                    crafted_item3 = ""     
                    
        if armour_item == 3:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Chain_Armour < 1 and inventory2.Soul_Dead < 5 and inventory2.Obsidian < 2:
                        crafted_item3 = "you don't have enough materials"
                    else:
                        crafted_item3 = "You have crafted black armour"  
                        inventory2.Chain_Armour = inventory2.Chain_Armour - 1
                        inventory2.Soul_Dead = inventory2.Soul_Dead - 5
                        inventory2.Obsidian = inventory2.Obsidian - 2
                        Combat2.P_health = Combat2.P_health + 50
                else:
                    crafted_item3 = ""    
                     
        if armour_item == 4:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Black_Armour < 1 and inventory2.Fire_Essence < 5:
                        crafted_item3 = "you don't have enough materials"
                    else:
                        crafted_item3 = "You have crafted molten armour"
                        inventory2.Black_Armour = inventory2.Black_Armour - 1
                        inventory2.Fire_Essence = inventory2.Fire_Essence - 5
                        Combat2.P_health = Combat2.P_Health + 120
                        Combat2.P_block = Combat2.P_block +20
                else:
                    crafted_item3 = ""
                    
        if armour_item == 5:
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Molten_Armour < 1 and inventory2.Void_Essence < 10:
                        crafted_item3 = "you don't have enough materials"
                    else:
                        crafted_item3 = "You have crafted amadantium plate"
                        inventory2.Molten_Armour = inventory2.Molten_Armour - 1
                        inventory2.Mana_Essence = inventory2.Mana_Essence - 10
                        Combat2.P_health = Combat2.P_health + 250
                else:
                    crafted_item3 = ""
      
        #This will select an item in the shield page
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

# if the selected item is selected it will look in the inventory to see if you have enough materials to craft the item
# if you have enough material it will craft the item and take the materials from the inventory                
        if shield_item == 1:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Wooden_Chunk < 5 and inventory2.Wooden_Stick < 2:
                        crafted_item2 = "you don't have enough materials"
                    else:
                        crafted_item2 = "You have crafted wooden shield"
                        inventory2.Wooden_Chunk = inventory2.Wooden_Chunk - 5
                        inventory2.Wooden_Stick = inventory2.Wooden_Stick - 2    
                        Combat2.P_block = Combat2.P_block + 3
                else:
                    crafted_item2 = "" 
                           
        if shield_item == 2:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Wooden_Shield < 1 and inventory2.Iron_Chunk < 5:
                        crafted_item2 = "you don't have enough materials"
                    else:
                        crafted_item2 = "You have crafted iron shield" 
                        inventory2.Wooden_Shield = inventory2.Wooden_Shield - 1
                        inventory2.Iron_Chunk = inventory2.IronChunk - 5
                        Combat2.P_block = Combat2.P_block + 5
                else:
                    crafted_item2 = "" 
                          
        if shield_item == 3:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Iron_Shield < 1 and inventory2.Mana_Essence < 10:
                        crafted_item2= "you don't have enough materials"
                    else:
                        crafted_item2 = "You have crafted null shield" 
                        inventory2.Iron_Shield = inventory2.Iron_Shield - 1
                        inventory2.Mana_Essence = inventory2.Mana_Essence - 10
                        Combat2.P_block = Combat2.P_block + 7
                else:
                    crafted_item2 = ""
                            
        if shield_item == 4:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Iron_Shield < 1 and inventory2.Null_Shield < 1 and inventory2.Gold_Ingot < 3:
                        crafted_item2 = "you don't have enough materials"
                    else:
                        crafted_item2 = "You have crafted gold shield"
                        inventory2.Iron_Shield = inventory2.Iron_Shield - 1
                        inventory2.Null_Shield = inventory2.Null_Shield - 1
                        inventory2.Gold_Ingot = inventory2.Gold_Ingot - 3
                        Combat2.P_block = Combat2.P_block + 30
                else:
                    crafted_item2 = ""
                    
        if shield_item == 5:
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Gold_Shield < 1 and inventory2.Void_Essence < 10:
                        crafted_item2 = "you don't have enough materials"
                    else:
                        crafted_item2 = "You have crafted war god's aegis"
                        inventory2.Gold_Shield = inventory2.Gold_Shield - 1
                        inventory2.Void_Essence = inventory2.Void_Essence - 10
                        Combat2.P_block = Combat2.P_block + 80
                else:
                    crafted_item2 = ""

        #This will select an item in the dagger page
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
                    if inventory2.Iron_Chunk < 1 and inventory2.Wooden_Stick < 1:
                        crafted_item5 = "you don't have enough materials"
                    else:
                        crafted_item5 = "You have crafted basic dagger"
                        inventory2.Iron_Chunk = inventory2.Iron_Chunk - 1
                        inventory2.Wooden_Stick = inventory2.Wooden_Stick  - 1 
                        Combat2.P_damage = Combat2.P_damage + 2 
                else:
                    crafted_item5 = ""  
                           
        if dagger_item == 2:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Basic_Dagger < 1 and inventory2.Mana_Essence < 3:
                        crafted_item5 = "you don't have enough materials"
                    else:
                        crafted_item5 = "You have crafted enchanted dagger"
                        inventory2.Basic_Dagger = inventory2.Basic_Dagger - 1
                        inventory2.Mana_Essence = inventory2.Mana_Essence - 3  
                        Combat2.piercing = Combat2.piercing + 8
                else:
                    crafted_item5 = "" 
                       
        if dagger_item == 3:    
            if tekst == "Craft":
                if isMouseWithinSpace(150, 850, 150, 60):
                    if inventory2.Enchanted_Dagger < 1 and inventory2.Scorpion_Poison < 3:
                        crafted_item5 = "you don't have enough materials"
                    else:
                        crafted_item5 = "You have crafted dagger of affliction"
                        inventory2.Enchanted_Dagger = inventory2.Enchanted_Dagger - 1
                        inventory2.Scorpion_Poison = inventory2.Scorpion_Poison - 3
                        Combat2.poison = Combat2.poison + 15
                else:
                    crafted_item5 = ""
