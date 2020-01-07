import inventory
def setup():
    fullScreen()
    global font, Scene, turn, dice, P_turn, M_turn, P_energy, P_health, P_block, M_energy, M_health, M_block, M_corruption, M_poison, M_fire, M_name, P_poison, P_corruption, P_fire, monster, energy, charging, P_gain, M_gain, M_charge, P_charge, damage, block, piercing, corruption, poison, fire, cleanse, heal, img_DeathGazer, img_VoidTentacle, img_VoidElemental, img_Voidling, img_CrimsonDragon, img_FireDrake, img_LavaGolem, img_LavaSlime, img_ghost, img_zombie, img_GoldenScarab, img_mummy, img_AncientSkeleton, img_GiantScorpion, img_basilisk, img_haunter, img_HauntedTree, img_GrimReaper, img_VoidSpawn, img_ManaGolem, img_SkeletonMage, img_ArcaneWolf, img_fairy, img_treant, img_skeleton, img_bear, img_wolf, img_slime, img_attack_5, img_attack_8, img_block_5, img_block_10, img_piercing, img_cleanse, img_corruption, img_fireball, img_heal, img_magic_missile, img_poison
    font = createFont('Arial', 32)
    Scene = 0
    turn = 0
    dice = 1
    P_turn = 0
    P_energy = 100
    P_health = 1000
    P_block = 100
    P_corruption = 0
    P_poison = 0
    P_fire = 0
    M_energy = 0
    M_health = 0
    M_block = 0
    M_corruption = 0
    M_poison = 0
    M_fire = 0
    M_turn = 0
    M_name = ""
    energy = 0
    damage = 0
    block = 0
    piercing = 0
    corruption = 0
    poison = 0
    fire = 0
    cleanse = 0
    heal = 0
    charging = 0
    M_charge = 0
    P_charge = 10
    P_gain = 5
    M_gain = 0
    img_attack_5 = loadImage("Attack_5.png")
    img_attack_8 = loadImage("Attack_8.png")
    img_block_5 = loadImage("Block_5.png")
    img_block_10 = loadImage("Block_10.png")
    img_piercing = loadImage("Piercing.png")
    img_cleanse = loadImage("Cleanse.png")
    img_corruption = loadImage("Corruption.png")
    img_fireball = loadImage("Fireball.png")
    img_heal = loadImage("Heal.png")
    img_magic_missile = loadImage("Magic_Missile.png")
    img_poison = loadImage("Poison.png")
    
    img_slime = loadImage("slime.png")
    img_wolf = loadImage("Wolf.png")
    img_bear = loadImage("Bear.png")
    img_skeleton = loadImage("skeleton.png")
    img_treant = loadImage("treant.png")
    img_fairy = loadImage("fairy.png")
    img_ArcaneWolf = loadImage("ArWolf.png")
    img_SkeletonMage = loadImage("skelMage.png")
    img_ManaGolem = loadImage("Magolem.png")
    img_VoidSpawn = loadImage("voidSpawn.png")
    img_ghost = loadImage("Ghost.png")
    img_zombie = loadImage("zombie.png")
    img_haunter = loadImage("haunter.png")
    img_HauntedTree = loadImage("Htree.png")
    img_GrimReaper = loadImage("Grimreap.png")
    img_GoldenScarab = loadImage("Golden Scarab.png")
    img_mummy = loadImage("Mummy.png")
    img_AncientSkeleton = loadImage("SkeletonAncient.png")
    img_GiantScorpion = loadImage("Scorpion.png")
    img_basilisk = loadImage("Basilisk.png")
    img_LavaSlime = loadImage("LavaSlime.png")
    img_LavaGolem = loadImage("LavaGolem.png")
    img_FireDrake = loadImage("FireDrake.png")
    img_CrimsonDragon = loadImage("CrimsonDragon.png")
    img_Voidling = loadImage("Voidling.png")
    img_VoidElemental = loadImage("VoidElemental.png")
    img_VoidTentacle = loadImage("VoidTentacle.png")
    img_DeathGazer = loadImage("DeathGazer.png")
    
    monster = 0


#Graphic stuff. Everything that has to be on the screen is here. 
def draw():
    global message, font, Scene, turn, drop, P_turn, M_turn, P_energy, P_health, P_block, M_energy, M_health, M_block, M_name, monster, energy, charging, damage, block, piercing, corruption, poison, fire, cleanse, heal, img_DeathGazer, img_VoidElemental, img_Voidling, img_CrimsonDragon, img_FireDrake, img_LavaGolem, img_LavaSlime, img_GoldenScarab, img_mummy, img_AncientSkeleton, img_GiantScorpion, img_basilisk, img_VoidSpawn, img_ghost, img_zombie, img_haunter, img_HauntedTree, img_GrimReaper, img_ManaGolem, img_SkeletonMage, img_fairy, img_treant, img_skeleton, img_bear, img_wolf, img_slime, img_attack_5, img_attack_8, img_block_5, img_block_10, img_piercing, img_cleanse, img_corruption, img_fireball, img_heal, img_magic_missile, img_poison
    if Scene == 0:  #scene 0 = combat page. Scene 1 = monster select page. Scene 2 = item drop page.
        background(0,0,0)
        textFont(font)
        fill(256,256,256)
        textSize(50)
        textAlign(CENTER)
    if turn == 0:
        P_turn = 0
        M_turn = 0
        
    rect(0,0,20,30)

    #texts for all the stats in the game.
    text('Player ' + str(P_turn), 1650, 100)
    text('Monster ' + str(M_turn), 1650, 200)
    text('End Turn', 1650, 1050)
    text('Player energy: ' + str(P_energy), 250, 100)
    text('Player health: ' + str(P_health), 750, 100)
    text('Player block: ' + str(P_block), 1250, 100)
    
    text('Monster energy: ' + str(M_energy), 250, 200)
    text('Monster health: ' + str(M_health), 750, 200)
    text('Monster block: ' + str(M_block), 1250, 200)
    
    text('Total damage: ' + str(damage), 1650, 300)
    text('Total block: ' + str(block), 1650, 350)
    text('Total piercing: ' + str(piercing), 1650, 400)
    text('Total corruption: ' + str(corruption), 1650, 450)
    text('Total poison: ' + str(poison), 1650, 500)
    text('Total fireballs: ' + str(fire), 1650, 550)
    
    text('Cleanse: ' + str(cleanse), 1200, 650)
    text('Heal: ' + str(heal), 1200, 700)
    text('Charging ' + str(charging), 1200, 750)
    
    text('Monster Corruption: ' + str(M_corruption), 1650, 650)
    text('Player Corruption: ' + str(P_corruption), 1650, 700)
    text('Monster Poison: ' + str(M_poison), 1650, 750)
    text('Player Poison: ' + str(P_poison), 1650, 800)
    text('Monster Fire: ' + str(M_fire), 1650, 850)
    text('Player Fire: ' + str(P_fire), 1650, 900)
    text('Total energy cost: ' + str(energy), 1650, 950)
    #text below is clickable (the code for that is further below. 
    text('Reset', 250, 1000)
    text('Change stats', 550, 1000)
    text('Drops', 900, 1000)
    text('Charge', 1200, 1000)
    
    image(img_attack_5, 50, 300) #images for cards.
    image(img_attack_8, 250, 300)
    image(img_block_5, 450, 300)
    image(img_block_10, 650, 300)
    image(img_piercing, 850, 300)
    image(img_cleanse, 1050, 300)
    image(img_corruption, 50, 600)
    image(img_fireball, 250, 600)
    image(img_heal, 450, 600)
    image(img_magic_missile, 650, 600)
    image(img_poison, 850, 600)
    
    if Scene == 1: #monster select page.
        background(0,0,0)
        textFont(font)
        fill(256,256,256)
        textSize(50)
        textAlign(CENTER)
        
        text('To battle!', 250, 1000)
        text('Selected: '+ str(M_name), 1500, 1000)
        text('Next Page', 1600, 700)
        
        image(img_slime, 50, 50)
        image(img_wolf, 250, 50)
        image(img_bear, 450, 50)
        image(img_skeleton, 650, 50)
        image(img_treant, 850, 50)
        image(img_fairy, 50, 350)
        image(img_ArcaneWolf, 250, 350)
        image(img_SkeletonMage, 450, 350)
        image(img_ManaGolem, 650, 350)
        image(img_VoidSpawn, 850, 350)
        image(img_ghost, 50, 650)
        image(img_zombie, 250, 650)
        image(img_haunter, 450, 650)
        image(img_HauntedTree, 650, 650)
        image(img_GrimReaper, 850, 650)
        
    if Scene == 3: #second page of monster select
        background(0,0,0)
        textFont(font)
        fill(256,256,256)
        textSize(50)
        textAlign(CENTER)
        
        text('Previous Page', 1600, 600)
        text('Selected: '+ str(M_name), 1500, 1000)
        text('To battle!', 250, 1000)
        
        image(img_GoldenScarab, 50, 50)
        image(img_mummy, 250, 50)
        image(img_AncientSkeleton, 450, 50)
        image(img_GiantScorpion, 650, 50)
        image(img_basilisk, 850, 50)
        image(img_LavaSlime, 50, 350)
        image(img_LavaGolem, 250, 350)
        image(img_FireDrake, 450, 350)
        image(img_CrimsonDragon, 650, 350)
        image(img_Voidling, 50, 650)
        image(img_VoidElemental, 250, 650)
        image(img_VoidTentacle, 450, 650)
        image(img_DeathGazer, 650, 650)
        
    if Scene == 2: #drop select page.
        background(0,0,0)
        textFont(font)
        fill(256,256,256)
        textSize(50)
        textAlign(CENTER)
        
        text('Drop page test', 600, 100)
        text('Back', 550, 1000)
        
        text('Drop page test', 600, 100)    

        if monster == 6:
                if dice == 1 or dice == 5 or dice == 4 or dice == 6:
                    textAlign(CENTER)
                    text("Mana Essence", width /2, height - 200)
        #             inventory.Mana_Essence = inventory.Mana_Essence + 1
                else:
                    textAlign(CENTER)
                    text("Mana Essence x2", width /2, height - 200)
        #             inventory.Mana_Essence = inventory.Mana_Essence + 2
        if monster == 1:
                if dice in range(1, 7):
                    textAlign(CENTER)
                    text("Nothing", width /2, height -200)
        
        if monster == 2:
                if dice == 1 or dice == 3 or dice == 4:
                    textAlign(CENTER)
                    text("Wolf Skin", width /2, height - 200)
        #             inventory.Wolf_Skin = inventory.Wolf_Skin + 1
                elif dice == 2 or dice == 5:
                    textAlign(CENTER)
                    text("Nothing", width /2, height - 200)
                else:
                    textAlign(CENTER)
                    text("Wolf Skin x2", width /2, height - 200)
        #             inventory.Wolf_Skin = inventory.Wolf_Skin + 2
                    
        if monster == 3:
                if dice == 1:
                    textAlign(CENTER)
                    text("Bear Skin", width /2, height - 200)
        #             inventory.Bear_Skin = inventory.Bear_Skin + 1
                elif dice == 2 or dice == 5:
                    textAlign(CENTER)
                    text("Nothing", width /2, height - 200)
                else:
                    textAlign(CENTER)
                    text("Bear Skin x2", width /2, height - 200)
        #             inventory.Bear_Skin = inventory.Bear_Skin + 2
                    
        if monster == 4:
                if dice == 1 or dice == 6:
                    textAlign(CENTER)
                    text("Iron Chunk", width /2, height - 200)
        #             inventory.Iron_Chunk = inventory.Iron_Chunk + 1
                elif dice == 2 or dice == 3:
                    textAlign(CENTER)
                    text("Wooden Stick", width /2, height - 200)
        #             inventory.Wooden_Stick = inventory.Wooden.Stick + 1
                elif dice == 4:
                    textAlign(CENTER)
                    text("Iron Chunk x2", width /2, height - 200)
        #             inventory.Iron_Chunk = inventory.Iron_Chunk + 2
                else:
                    textAlign(CENTER)
                    text("Soul of the Dead", width /2, height - 200)
        #             inventory.Soul_Dead = inventory.Soul_Dead + 1
                    
        if monster == 5:
                if dice == 3 or dice == 5:
                    textAlign(CENTER)
                    text("Wooden Chunk x3", width /2, height - 200)
        #             inventory.Wooden_Chunk = inventory.Wooden_Chunk + 3
                elif dice == 4 or dice == 6:
                    textAlign(CENTER)
                    text("Wooden Stick x3", width /2, height - 200)
        #             inventory.Wooden_Stick = inventory.Wooden_Stick + 3
                else:
                    textAlign(CENTER)
                    text("Wooden Stick", width /2, height - 200)
        #             inventory.Wooden_Stick = inventory.Wooden_Stick + 1
                    
        if monster == 7:
                if dice == 1 or dice == 3 or dice == 4:
                    textAlign(CENTER)
                    text("Enchanted Wolf Skin", width /2, height - 200)
        #             inventory.Enchanted_Wolf = inventory.Enchanted_Wolf + 1
                elif dice == 2 or dice == 5:
                    textAlign(CENTER)
                    text("Mana Essence", width /2, height - 200)
        #             inventory.Mana_Essence = inventory.Mana_Essence + 1
                else:
                    textAlign(CENTER)
                    text("Enchanted Wolf Skin x2", width /2, height - 200)
        #             inventory.Enchanted_Wolf = inventory.Enchanted_Wolf + 2
                    
        if monster == 8:
                if dice == 3 or dice == 4:
                    textAlign(CENTER)
                    text("Soulf od the Dead", width /2, height - 200)
        #             inventory.Soul_Dead = inventory.Soul_Dead + 1
                elif dice == 2:
                    textAlign(CENTER)
                    text("Mana Essence", width /2, height - 200)
        #             inventory.Mana_Essence = inventory.Mana_Essence + 1
                elif dice == 5 or dice == 6:
                    textAlign(CENTER)
                    text("Soul of the Dead x2", width /2, height - 200)
        #             inventory.Soul_Dead = inventory.Soul_Dead + 2
                else:
                    textAlign(CENTER)
                    text("Mana Essence x2", width /2, height - 200)
        #             inventory.Mana_Essence = inventory.Mana_Essence + 2
                    
        if monster == 9:
                if dice == 1 or dice == 2:
                    textAlign(CENTER)
                    text("Mana Essence x2", width /2, height - 200)
        #             inventory.Mana_Essence = inventory.Mana_Essence + 2
                else:
                    textAlign(CENTER)
                    text("Obsidian", width /2, height - 200)
        #             inventory.Obsidian = inventory.Obsidian + 1
        if monster == 10:
                if dice == 2 or dice == 4:
                    textAlign(CENTER)
                    text("Void Energy x2", width /2, height - 200)
        #             inventory.Void_Essence = inventory.Void_Essence + 2
                else:
                    textAlign(CENTER)
                    text("Void Energy", width /2, height - 200)
        #             inventory.Void_Essence = inventory.Void_Essence + 1
                    
        if monster == 11:
                if dice == 1 or dice == 3 or dice == 6:
                    textAlign(CENTER)
                    text("Soul of the Dead", width /2, height - 200)
        #             inventory.Soul_Dead = inventory.Soul_Dead + 1
                elif dice == 2 or dice == 4:
                    textAlign(CENTER)
                    text("Soul of the Dead x3", width /2, height - 200)
        #             inventory.Soul_Dead = inventory.Soul_Dead + 3
                else:
                    textAlign(CENTER)
                    text("Wolf Skin x2", width /2, height - 200)
        #             inventory.Wolf_Skin = inventory.Wolf_Skin + 2
                    
        if monster == 12:
                if dice in range(1,6 +1):
                    textAlign(CENTER)
                    text("Soul of the Dead x2", width /2, height - 200)
        #             inventory.Soul_Dead = inventory.Soul_Dead + 2
                    
        if monster == 13:
                if dice == 3 or dice == 6 or dice == 1:
                    textAlign(CENTER)
                    text("Soul of the Dead", width /2, height - 200)
        #             inventory.Soul_Dead = inventory.Soul_Dead + 1
                else:
                    textAlign(CENTER)
                    text("Haunted Spirit", width /2, height - 200)
        #             inventory.Haunted_Spirit = inventory.Haunted_Spirit + 1
        if monster == 14:
                if dice == 1 or dice == 6:
                    textAlign(CENTER)
                    text("Haunted Spirit", width /2, height - 200)
        #             inventory.Haunted_Spirit = inventory.Haunted_Spirit + 1
                elif dice == 3:
                    textAlign(CENTER)
                    text("Cursed Wood x2", width /2, height - 200)
        #             inventory.Cursed_Wood = inventory.Cursed_Wood + 2
                else:
                    textAlign(CENTER)
                    text("Cursed Wood", width /2, height - 200)
        #             inventory.Cursed_Wood = inventory.Cursed_Wood + 1
                    
        if monster == 16:
                if dice == 3 or dice == 5:
                    textAlign(CENTER)
                    text("Gold Ingot x2", width /2, height - 200)
        #             inventory.Gold_Ingot = inventory.Gold_Ingot + 2
                else:
                    textAlign(CENTER)
                    text("Gold Ingot", width /2, height - 200)
        #             inventory.Gold_Ingot = inventory.Gold_Ingot + 1
                    
        if monster == 18:
                if dice == 2 or dice == 4:
                    textAlign(CENTER)
                    text("Soul of the Dead x5", width /2, height - 200)
        #             inventory.Soul_Dead = inventory.Soul_Dead + 5
                else:
                    textAlign(CENTER)
                    text("Gold Ingot", width /2, height - 200)
        #             inventory.Gold_Ingot = inventory.Gold_Ingot + 1
                    
        if monster == 19:
                if dice in range(1, 6+1):
                    textAlign(CENTER)
                    text("Scorpion Poison", width /2, height - 200)
        #             inventory.Scorpion_Poison = inventory.Scorpion_Poison + 1
                    
        if monster == 17:
                if dice in range(1,6 +1):
                    textAlign(CENTER)
                    text("Soul of the Dead x2", width /2, height - 200)
        #             inventory.Soul_Dead = inventory.Soul_Dead + 2
                    
        if monster == 21 or monster == 22 or monster == 23:
                if dice == 1 or dice == 3 or dice == 5:
                    textAlign(CENTER)
                    text("Fire Essence", width /2, height - 200)
        #             inventory.Fire_Essence = inventory.Fire_Essence + 1
                elif dice == 2 or dice == 4:
                    textAlign(CENTER)
                    text("Fire Essence x2", width /2, height - 200) 
        #             inventory.Fire_Essence = inventory.Fire_Essence + 2
                else:
                    textAlign(CENTER)
                    text("Fire Essence x3", width /2, height - 200)
        #             inventory.Fire_Essence = inventory.Fire_Essence + 3
                
        if monster == 25 or monster == 26 or monster == 27:
                if dice == 1 or dice == 3 or dice == 5:
                    textAlign(CENTER)
                    text("Void Essence", width /2, height - 200)
        #             inventory.Void_Essence = inventory.Void_Essence + 1
                elif dice == 2 or dice == 4:
                    textAlign(CENTER)
                    text("Void Essence x2", width /2, height - 200)
        #             inventory.Void_Essence = inventory.Void_Essence + 2
                else:
                    textAlign(CENTER)
                    text("Void Essence x3", width /2, height - 200)
        #             inventory.Void_Essence = inventory.Void_Essence + 3
        

#function to enable mouse clicking in specific locations.        
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False 

#I'm not gonna bother explaining. This is to calculate all the stats in the game. Have fun reading. 
def mousePressed():
    global Scene, dice, P_energy, M_energy, M_turn, P_turn, M_health, M_block, M_corruption, M_poison, M_fire, M_name, P_health, P_block, P_corruption, P_poison, P_fire, monster, energy, P_gain, M_gain, M_charge, P_charge, charging, corruption, poison, damage, fire, cleanse, heal, block, turn, piercing
    if Scene == 0:
        if isMouseWithinSpace(1550, 50, 200, 50):
            turn = 1
            P_turn = 1
            M_turn = 0
        if isMouseWithinSpace(1550, 150, 200, 50):
            turn = 2
            M_turn = 1
            P_turn = 0
        if isMouseWithinSpace(150, 950, 200, 50):
            damage = 0
            block = 0
            piercing = 0
            corruption = 0
            poison = 0
            fire = 0
            cleanse = 0
            heal = 0
            energy = 0
            charging = 0
        
        if isMouseWithinSpace(400, 950, 300, 50):
            Scene = 1
        
        if isMouseWithinSpace(800, 950, 200, 50):
            Scene = 2
            dice = int(random(1,6))
        
        if isMouseWithinSpace(1100, 950, 200, 50) and charging == 0:
            charging = 1
    
        if turn == 1:
            if isMouseWithinSpace(50, 300, 172, 238):
                damage = damage + 5
                energy = energy + 5
            if isMouseWithinSpace(250, 300, 172, 238):
                damage = damage + 10
                energy = energy + 8
            if isMouseWithinSpace(450, 300, 172, 238):
                block = block + 5
                energy = energy + 10
            if isMouseWithinSpace(650, 300, 172, 238):
                block = block + 10
                energy = energy + 15
            if isMouseWithinSpace(850, 300, 172, 238):
                piercing = piercing + 5
                energy = energy + 7
            if isMouseWithinSpace(50, 600, 172, 238):
                corruption = corruption + 1
                energy = energy + 10
            if isMouseWithinSpace(850, 600, 172, 238):
                poison = poison + 1
                energy = energy + 5
            if isMouseWithinSpace(250, 600, 172, 238):
                damage = damage + 5
                fire = fire + 1
                energy = energy + 6
            if isMouseWithinSpace(450, 600, 172, 238):
                heal = heal + 1
                energy = energy + 15
            if isMouseWithinSpace(650, 600, 172, 238):
                damage = damage + 5
                energy = energy + 5
            if isMouseWithinSpace(1050, 300, 172, 238):
                cleanse = cleanse + 1 
                energy = energy + 5
        
    
        if turn == 2: 
            if isMouseWithinSpace(50, 300, 172, 238):
                if monster == 16:
                    damage = damage + 10
                elif monster == 18:
                    damage = damage + 10
                elif monster == 21:
                    damage = damage + 10
                elif monster == 22:
                    damage = damage + 10
                elif monster == 23:
                    damage = damage + 10
                elif monster == 24:
                    damage = damage + 15
                elif monster == 25:
                    damage = damage + 15
                elif monster == 27:
                    damage = damage + 45
                elif monster == 26:
                    damage = damage + 20
                elif monster == 28:
                    damage = damage + 60
                else:
                    damage = damage + 5
                energy = energy + 5
            if isMouseWithinSpace(250, 300, 172, 238):
                if monster == 16:
                    damage = damage + 20
                elif monster == 18:
                    damage = damage + 20
                elif monster == 21:
                    damage = damage + 20
                elif monster == 22:
                    damage = damage + 20
                elif monster == 23:
                    damage = damage + 20
                elif monster == 24:
                    damage = damage + 30
                elif monster == 25:
                    damage = damage + 30
                elif monster == 27:
                    damage = damage + 50
                elif monster == 26:
                    damage = damage + 40
                elif monster == 28:
                    damage = damage + 80
                else:
                    damage = damage + 10
                energy = energy + 8
            if isMouseWithinSpace(450, 300, 172, 238):
                if monster == 17:
                    block = block + 10
                elif monster == 21:
                    block = block + 10
                elif monster == 22:
                    block = block + 10
                elif monster == 23:
                    block = block + 10
                elif monster == 24:
                    block = block + 15
                elif monster == 25:
                    block = block + 15
                elif monster == 26:
                    block = block + 20
                elif monster == 28:
                    block = block + 20
                else:
                    block = block + 5
                energy = energy + 10
            if isMouseWithinSpace(650, 300, 172, 238):
                if monster == 17:
                    block = block + 20
                elif monster == 21:
                    block = block + 20
                elif monster == 22:
                    block = block + 20
                elif monster == 23:
                    block = block + 20
                elif monster == 24:
                    block = block + 30
                elif monster == 25:
                    block = block + 30
                elif monster == 26:
                    block = block + 40
                elif monster == 28:
                    block = block + 40
                else:
                    block = block + 10
                energy = energy + 15
            if isMouseWithinSpace(850, 300, 172, 238):
                if monster == 16:
                    piercing = piercing + 10
                elif monster == 18:
                    piercing = piercing + 10
                elif monster == 21:
                    piercing = piercing + 10
                elif monster == 22:
                    piercing = piercing + 10
                elif monster == 23:
                    piercing = piercing + 10
                elif monster == 24:
                    piercing = piercing + 15
                elif monster == 25:
                    piercing = piercing + 15
                elif monster == 26:
                    piercing = piercing + 20
                elif monster == 28:
                    piercing = piercing + 20
                else:
                    piercing = piercing + 5
                energy = energy + 7
            if isMouseWithinSpace(50, 600, 172, 238):
                corruption = corruption + 1
                energy = energy + 10
            if isMouseWithinSpace(850, 600, 172, 238):
                poison = poison + 1
                energy = energy + 5
            if isMouseWithinSpace(250, 600, 172, 238):
                if monster == 16:
                    damage = damage + 10
                elif monster == 18:
                    damage = damage + 10
                elif monster == 21:
                    damage = damage + 10
                elif monster == 22:
                    damage = damage + 10
                elif monster == 23:
                    damage = damage + 10
                elif monster == 24:
                    damage = damage + 15
                elif monster == 25:
                    damage = damage + 15
                elif monster == 26:
                    damage = damage + 20
                elif monster == 28:
                    damage = damage + 20
                else:
                    damage = damage + 5
                    fire = fire + 1
                energy = energy + 6
            if isMouseWithinSpace(450, 600, 172, 238):
                if monster == 21:
                    heal = heal + 2
                elif monster == 22:
                    heal = heal + 2
                elif monster == 23:
                    heal = heal + 2
                elif monster == 24:
                    heal = heal + 3
                elif monster == 25:
                    heal = heal + 3
                elif monster == 26:
                    heal = heal + 4
                elif monster == 28:
                    heal = heal + 4
                else:
                    heal = heal + 1
                energy = energy + 15
            if isMouseWithinSpace(650, 600, 172, 238):
                if monster == 13:
                    damage = damage + 10
                elif monster == 16:
                    damage = damage + 10
                elif monster == 18:
                    damage = damage + 10
                elif monster == 21:
                    damage = damage + 10
                elif monster == 22:
                    damage = damage + 10
                elif monster == 23:
                    damage = damage + 10
                elif monster == 24:
                    damage = damage + 15
                elif monster == 25:
                    damage = damage + 15
                elif monster == 26:
                    damage = damage + 20
                elif monster == 28:
                    damage = damage + 20
                else:
                    damage = damage + 5
                energy = energy + 5
            if isMouseWithinSpace(1050, 300, 172, 238):
                cleanse = cleanse + 1 
                energy = energy + 5
            
        #Dit is voor de End Turn
        if isMouseWithinSpace(1550, 1000, 200, 50):
            if M_block < 0:
                M_block = 0
            if P_block < 0:
                P_block = 0
    
            if turn == 1:
                if charging == 1:
                    P_energy = P_energy + P_charge
                if charging == 0:
                    P_energy = P_energy + P_gain
                if cleanse > 0:
                    P_poison = 0
                    P_corruption = 0
                    P_fire = 0
                if M_poison > 0:
                    damage = damage + 2
                    M_poison = M_poison - 1
                    if M_poison < 0:
                        M_poison = 0
                if M_corruption > 0:
                    damage = damage + 5
                    M_corruption = M_corruption - 1
                    if M_corruption < 0:
                        M_corruption = 0
                if M_fire > 0:
                    damage = damage + 1
                    M_fire = M_fire - 1
                    if M_fire < 0:
                        M_fire = 0
                P_energy = P_energy - energy
                P_block = P_block + block
                P_health = P_health + heal * 15
                M_block = M_block - damage
                if monster != 28:
                    M_health = M_health - piercing
                M_corruption = M_corruption + (corruption * 4)
                M_poison = M_poison + (poison * 5)
                M_fire = M_fire + (fire * 3)
                if M_block < 0:
                    M_health = M_health + M_block
                    M_block = 0 
                damage = 0
                block = 0
                piercing = 0
                corruption = 0
                poison = 0
                fire = 0
                heal = 0
                cleanse = 0
                turn = 0
                energy = 0
                charging = 0
    
            if  turn == 2:
                if charging == 1:
                    M_energy = M_energy + M_charge
                if charging == 0:
                    M_energy = M_energy + M_gain
                if cleanse > 0:
                    M_poison = 0
                    M_corruption = 0
                    M_fire = 0
                if P_poison > 0:
                    if monster == 19:
                        damage = damage + 4
                    elif monster == 16:
                        damage = damage + 4
                    elif monster == 18:
                        damage = damage + 4
                    elif monster == 20:
                        damage = damage + 4
                    elif monster == 21:
                        damage = damage + 4
                    elif monster == 22:
                        damage = damage + 4
                    elif monster == 23:
                        damage = damage + 4
                    elif monster == 24:
                        damage = damage + 6
                    elif monster == 25:
                        damage = damage + 6
                    elif monster == 26:
                        damage = damage + 8
                    elif monster == 28:
                        damage = damage + 8
                    else:
                        damage = damage + 2
                    P_poison = P_poison - 1
                    if P_poison < 0:
                        P_poison = 0
                if P_corruption > 0:
                    if monster == 16:
                        damage = damage + 10
                    elif monster == 18:
                        damage = damage + 10
                    elif monster == 19:
                        damage = damage + 10
                    elif monster == 20:
                        damage = damage + 10
                    elif monster == 21:
                        damage = damage + 10
                    elif monster == 22:
                        damage = damage + 10
                    elif monster == 23:
                        damage = damage + 10
                    elif monster == 24:
                        damage = damage + 15
                    elif monster == 25:
                        damage = damage + 15
                    elif monster == 26:
                        damage = damage + 20
                    elif monster == 28:
                        damage = damage + 20
                    else:
                        damage = damage + 5
                    P_corruption = P_corruption - 1
                    if P_corruption < 0:
                        P_corruption = 0
                if P_fire > 0:
                    if monster == 16:
                        damage = damage + 2
                    elif monster == 18:
                        damage = damage + 2
                    elif monster == 20:
                        damage = damage + 2
                    elif monster == 21:
                        damage = damage + 2
                    elif monster == 22:
                        damage = damage + 2
                    elif monster == 23:
                        damage = damage + 2
                    elif monster == 24:
                        damage = damage + 3
                    elif monster == 25:
                        damage = damage + 3
                    elif monster == 26:
                        damage = damage + 4
                    elif monster == 26:
                        damage = damage + 4
                    else:
                        damage = damage + 1
                    P_fire = P_fire - 1
                    if P_fire < 0:
                        P_fire = 0
                M_energy = M_energy - energy
                M_block = M_block + block
                M_health = M_health + heal * 15
                P_block = P_block - damage
                P_health = P_health - piercing
                P_corruption = P_corruption + (corruption * 4)
                P_poison = P_poison + (poison * 5)
                P_fire = P_fire + (fire * 3)
                if P_block < 0:
                    P_health = P_health + P_block
                    P_block = 0
            damage = 0
            block = 0
            piercing = 0
            corruption = 0
            poison = 0
            fire = 0
            heal = 0
            cleanse = 0
            turn = 0
            energy = 0
            charging = 0

    #Code for clicking monster cards.      
    if Scene == 1:
        if isMouseWithinSpace(150, 950, 200, 50):
            Scene = 0
        if isMouseWithinSpace(1500, 650, 200, 50):
            Scene = 3 
            
        if isMouseWithinSpace(50, 50, 172, 238):
            monster = 1
        if isMouseWithinSpace(250, 50, 172, 238):
            monster = 2
            if monster == 2:
                if dice == 1 or dice == 3 or dice == 4:
    #             textAlign(CENTER)
    #             text("Wolf Skin", width /2, height - 200)
                    inventory.Wolf_Skin = inventory.Wolf_Skin + 1
                elif dice == 2 or dice == 5:
    #             textAlign(CENTER)
    #             text("Nothing", width /2, height - 200)
                    inventory.Wolf_Skin = inventory.Wolf_Skin + 0

                else:
    #             textAlign(CENTER)
    #             text("Wolf Skin x2", width /2, height - 200)
                    inventory.Wolf_Skin = inventory.Wolf_Skin + 2
        if isMouseWithinSpace(450, 50, 172, 238):
            monster = 3
            if monster == 3:
                if dice == 1:
    #             textAlign(CENTER)
    #             text("Bear Skin", width /2, height - 200)
                    inventory.Bear_Skin = inventory.Bear_Skin + 1
                elif dice == 2 or dice == 5:
    #             textAlign(CENTER)
    #             text("Nothing", width /2, height - 200)
                    inventory.Bear_Skin = inventory.Bear_Skin + 0
                else:
    #             textAlign(CENTER)
    #             text("Bear Skin x2", width /2, height - 200)
                    inventory.Bear_Skin = inventory.Bear_Skin + 2
        if isMouseWithinSpace(650, 50, 172, 238):
            monster = 4
            if monster == 4:
                if dice == 1 or dice == 6:
    #             textAlign(CENTER)
    #             text("Iron Chunk", width /2, height - 200)
                    inventory.Iron_Chunk = inventory.Iron_Chunk + 1
                elif dice == 2 or dice == 3:
    #             textAlign(CENTER)
    #             text("Wooden Stick", width /2, height - 200)
                    inventory.Wooden_Stick = inventory.Wooden.Stick + 1
                elif dice == 4:
    #             textAlign(CENTER)
    #             text("Iron Chunk x2", width /2, height - 200)
                    inventory.Iron_Chunk = inventory.Iron_Chunk + 2
                else:
    #             textAlign(CENTER)
    #             text("Soul of the Dead", width /2, height - 200)
                    inventory.Soul_Dead = inventory.Soul_Dead + 1
        if isMouseWithinSpace(850, 50, 172, 238):
            monster = 5
            if monster == 5:
                if dice == 3 or dice == 5:
    #             textAlign(CENTER)
    #             text("Wooden Chunk x3", width /2, height - 200)
                    inventory.Wooden_Chunk = inventory.Wooden_Chunk + 3
                elif dice == 4 or dice == 6:
    #             textAlign(CENTER)
    #             text("Wooden Stick x3", width /2, height - 200)
                    inventory.Wooden_Stick = inventory.Wooden_Stick + 3
                else:
    #             textAlign(CENTER)
    #             text("Wooden Stick", width /2, height - 200)
                    inventory.Wooden_Stick = inventory.Wooden_Stick + 1
        if isMouseWithinSpace(50, 350, 172, 238):
            monster = 6
            if monster == 6:
                if dice == 1 or dice == 5 or dice == 4 or dice == 6:
                   # textAlign(CENTER)
                   # text("Mana Essence", width /2, height - 200)
                    inventory.Mana_Essence = inventory.Mana_Essence + 1
                else:
                    #textAlign(CENTER)
                    #text("Mana Essence x2", width /2, height - 200)
                    inventory.Mana_Essence = inventory.Mana_Essence + 2
        if isMouseWithinSpace(250, 350, 172, 238):
            monster = 7
            if monster == 7:
                if dice == 1 or dice == 3 or dice == 4:
    #             textAlign(CENTER)
    #             text("Enchanted Wolf Skin", width /2, height - 200)
                    inventory.Enchanted_Wolf = inventory.Enchanted_Wolf + 1
                elif dice == 2 or dice == 5:
    #             textAlign(CENTER)
    #             text("Mana Essence", width /2, height - 200)
                    inventory.Mana_Essence = inventory.Mana_Essence + 1
                else:
    #             textAlign(CENTER)
    #             text("Enchanted Wolf Skin x2", width /2, height - 200)
                    inventory.Enchanted_Wolf = inventory.Enchanted_Wolf + 2
        if isMouseWithinSpace(450, 350, 172, 238):
            monster = 8
            if monster == 8:
                if dice == 3 or dice == 4:
    #             textAlign(CENTER)
    #             text("Soulf od the Dead", width /2, height - 200)
                    inventory.Soul_Dead = inventory.Soul_Dead + 1
                elif dice == 2:
    #             textAlign(CENTER)
    #             text("Mana Essence", width /2, height - 200)
                    inventory.Mana_Essence = inventory.Mana_Essence + 1
                elif dice == 5 or dice == 6:
    #             textAlign(CENTER)
    #             text("Soul of the Dead x2", width /2, height - 200)
                    inventory.Soul_Dead = inventory.Soul_Dead + 2
                else:
    #             textAlign(CENTER)
    #             text("Mana Essence x2", width /2, height - 200)
                    inventory.Mana_Essence = inventory.Mana_Essence + 2
        if isMouseWithinSpace(650, 350, 172, 238):
            monster = 9
            if monster == 9:
                if dice == 1 or dice == 2:
    #             textAlign(CENTER)
    #             text("Mana Essence x2", width /2, height - 200)
                    inventory.Mana_Essence = inventory.Mana_Essence + 2
                else:
    #             textAlign(CENTER)
    #             text("Obsidian", width /2, height - 200)
                    inventory.Obsidian = inventory.Obsidian + 1
        if isMouseWithinSpace(850, 350, 172, 238):
            monster = 10
            if monster == 10:
                if dice == 2 or dice == 4:
    #             textAlign(CENTER)
    #             text("Void Energy x2", width /2, height - 200)
                    inventory.Void_Essence = inventory.Void_Essence + 2
                else:
    #             textAlign(CENTER)
    #             text("Void Energy", width /2, height - 200)
                    inventory.Void_Essence = inventory.Void_Essence + 1
        if isMouseWithinSpace(50, 650, 172, 238):
            monster = 11
            if monster == 11:
                if dice == 1 or dice == 3 or dice == 6:
    #             textAlign(CENTER)
    #             text("Soul of the Dead", width /2, height - 200)
                    inventory.Soul_Dead = inventory.Soul_Dead + 1
                elif dice == 2 or dice == 4:
    #             textAlign(CENTER)
    #             text("Soul of the Dead x3", width /2, height - 200)
                    inventory.Soul_Dead = inventory.Soul_Dead + 3
                else:
    #             textAlign(CENTER)
    #             text("Wolf Skin x2", width /2, height - 200)
                    inventory.Wolf_Skin = inventory.Wolf_Skin + 2
        if isMouseWithinSpace(250, 650, 172, 238):
            monster = 12
            if monster == 12:
                if dice in range(1,6 +1):
        #             textAlign(CENTER)
    #             text("Soul of the Dead x2", width /2, height - 200)
                    inventory.Soul_Dead = inventory.Soul_Dead + 2
        if isMouseWithinSpace(450, 650, 172, 238):
            monster = 13
            if monster == 13:
                if dice == 3 or dice == 6 or dice == 1:
    #             textAlign(CENTER)
    #             text("Soul of the Dead", width /2, height - 200)
                    inventory.Soul_Dead = inventory.Soul_Dead + 1
                else:
    #             textAlign(CENTER)
    #             text("Haunted Spirit", width /2, height - 200)
                    inventory.Haunted_Spirit = inventory.Haunted_Spirit + 1
        if isMouseWithinSpace(650, 650, 172, 238):
            monster = 14
            if monster == 14:
                if dice == 1 or dice == 6:
    #             textAlign(CENTER)
    #             text("Haunted Spirit", width /2, height - 200)
                    inventory.Haunted_Spirit = inventory.Haunted_Spirit + 1
                elif dice == 3:
    #             textAlign(CENTER)
    #             text("Cursed Wood x2", width /2, height - 200)
                    inventory.Cursed_Wood = inventory.Cursed_Wood + 2
                else:
    #             textAlign(CENTER)
    #             text("Cursed Wood", width /2, height - 200)
                    inventory.Cursed_Wood = inventory.Cursed_Wood + 1
        if isMouseWithinSpace(850, 650, 172, 238):
            monster = 15
            
        

        #Monster stats: Forest
        if monster == 1:
            M_energy = 5
            M_health = 10
            M_charge = 10
            M_gain = 5
            M_name = "Slime"
        
        if monster == 2:
            M_energy = 5
            M_health = 20
            M_charge = 10
            M_gain = 5
            M_name = "Wolf"
        
        if monster == 3:
            M_energy = 5
            M_health = 30
            M_bonus_char = 0
            M_gain = 5
            M_name = "Bear"
        
        if monster == 4:
            M_energy = 5
            M_health = 25
            M_charge = 10
            M_gain = 5
            M_name = "Skeleton"
            
        if monster == 5:
            M_energy = 5
            M_health = 30
            M_charge = 10
            M_gain = 5
            M_name = "Treant"
        
        #Monster stats: Mystic Forest   
        if monster == 6:
            M_energy = 15
            M_health = 30
            M_charge = 15
            M_gain = 10
            M_name = "Fairy"
        
        if monster == 7:
            M_energy = 5
            M_health = 60
            M_charge = 10
            M_gain = 5
            M_name = "ArcaneWolf"
            
        if monster == 8:
            M_energy = 15
            M_health = 40
            M_charge = 15
            M_gain = 10
            M_name = "Skeleton Mage"
        
        if monster == 9:
            M_energy = 15
            M_health = 100
            M_charge = 15
            M_gain = 10
            M_name = "Mana Golem"
        
        if monster == 10:
            M_energy = 20
            M_health = 200
            M_charge = 20
            M_gain = 15
            M_name = "Void Spawn"
        
        if monster == 11: #SPECIAL - Only takes damage from magic cards (not ready yet)
            M_energy = 10
            M_health = 50
            M_charge = 10
            M_gain = 5
            M_name = "Ghost"
        
        if monster == 12:
            M_energy = 15
            M_health = 120
            M_charge = 15
            M_gain = 10
            M_name = "Zombie"
        
        if monster == 13: #SPECIAL - Double damage on magic cards (READY)
            M_energy = 20
            M_health = 100
            M_charge = 25
            M_gain = 10
            M_name = "Haunter"
            
        if monster == 14:
            M_energy = 20
            M_health = 170
            M_charge = 15
            M_gain = 10
            M_name = "Haunted Tree"
        
        if monster == 15:
            M_energy = 20
            M_health = 250
            M_charge = 15
            M_gain = 10
            M_name = "Grim Reaper"

        
        
        
    if Scene == 2:
        if isMouseWithinSpace(450, 950, 200, 50):
            Scene = 0
            
    if Scene == 3:
            if isMouseWithinSpace(1500, 550, 200, 50):
                Scene = 1
            if isMouseWithinSpace(150, 950, 200, 50):
                Scene = 0
                
            if isMouseWithinSpace(50, 50, 172, 238):
                monster = 16
                if monster == 16:
                    if dice == 3 or dice == 5:
    #             textAlign(CENTER)
    #             text("Gold Ingot x2", width /2, height - 200)
                        inventory.Gold_Ingot = inventory.Gold_Ingot + 2
                    else:
    #             textAlign(CENTER)
    #             text("Gold Ingot", width /2, height - 200)
                        inventory.Gold_Ingot = inventory.Gold_Ingot + 1
            if isMouseWithinSpace(250, 50, 172, 238):
                monster = 17
                if monster == 17:
                    if dice in range(1,6 +1):
    #             textAlign(CENTER)
    #             text("Soul of the Dead x2", width /2, height - 200)
                        inventory.Soul_Dead = inventory.Soul_Dead + 2
            if isMouseWithinSpace(450, 50, 172, 238):
                monster = 18
                if monster == 18:
                    if dice == 2 or dice == 4:
    #             textAlign(CENTER)
    #             text("Soul of the Dead x5", width /2, height - 200)
                        inventory.Soul_Dead = inventory.Soul_Dead + 5
                    else:
    #             textAlign(CENTER)
    #             text("Gold Ingot", width /2, height - 200)
                        inventory.Gold_Ingot = inventory.Gold_Ingot + 1
            if isMouseWithinSpace(650, 50, 172, 238):
                monster = 19
                if monster == 19:
                    if dice in range(1, 6+1):
    #             textAlign(CENTER)
    #             text("Scorpion Poison", width /2, height - 200)
                        inventory.Scorpion_Poison = inventory.Scorpion_Poison + 1
            if isMouseWithinSpace(850, 50, 172, 238):
                monster = 20
            if isMouseWithinSpace(50, 350, 172, 238):
                monster = 21
                if monster == 21 or monster == 22 or monster == 23:
                    if dice == 1 or dice == 3 or dice == 5:
    #             textAlign(CENTER)
    #             text("Fire Essence", width /2, height - 200)
                        inventory.Fire_Essence = inventory.Fire_Essence + 1
                    elif dice == 2 or dice == 4:
        #             textAlign(CENTER)
    #             text("Fire Essence x2", width /2, height - 200) 
                        inventory.Fire_Essence = inventory.Fire_Essence + 2
                    else:
    #             textAlign(CENTER)
    #             text("Fire Essence x3", width /2, height - 200)
                        inventory.Fire_Essence = inventory.Fire_Essence + 3
            if isMouseWithinSpace(250, 350, 172, 238):
                monster = 22
                if monster == 21 or monster == 22 or monster == 23:
                    if dice == 1 or dice == 3 or dice == 5:
    #             textAlign(CENTER)
    #             text("Fire Essence", width /2, height - 200)
                        inventory.Fire_Essence = inventory.Fire_Essence + 1
                    elif dice == 2 or dice == 4:
        #             textAlign(CENTER)
    #             text("Fire Essence x2", width /2, height - 200) 
                        inventory.Fire_Essence = inventory.Fire_Essence + 2
                    else:
    #             textAlign(CENTER)
    #             text("Fire Essence x3", width /2, height - 200)
                        inventory.Fire_Essence = inventory.Fire_Essence + 3
            if isMouseWithinSpace(450, 350, 172, 238):
                monster = 23
                if monster == 21 or monster == 22 or monster == 23:
                    if dice == 1 or dice == 3 or dice == 5:
    #             textAlign(CENTER)
    #             text("Fire Essence", width /2, height - 200)
                        inventory.Fire_Essence = inventory.Fire_Essence + 1
                    elif dice == 2 or dice == 4:
        #             textAlign(CENTER)
    #             text("Fire Essence x2", width /2, height - 200) 
                        inventory.Fire_Essence = inventory.Fire_Essence + 2
                    else:
    #             textAlign(CENTER)
    #             text("Fire Essence x3", width /2, height - 200)
                        inventory.Fire_Essence = inventory.Fire_Essence + 3
            if isMouseWithinSpace(650, 350, 172, 238):
                monster = 24
            if isMouseWithinSpace(50, 650, 172, 238):
                monster = 25
                if monster == 25 or monster == 26 or monster == 27:
                    if dice == 1 or dice == 3 or dice == 5:
    #             textAlign(CENTER)
    #             text("Void Essence", width /2, height - 200)
                        inventory.Void_Essence = inventory.Void_Essence + 1
                    elif dice == 2 or dice == 4:
        #             textAlign(CENTER)
    #             text("Void Essence x2", width /2, height - 200)
                        inventory.Void_Essence = inventory.Void_Essence + 2
                    else:
    #             textAlign(CENTER)
    #             text("Void Essence x3", width /2, height - 200)
                        inventory.Void_Essence = inventory.Void_Essence + 3
            if isMouseWithinSpace(250, 650, 172, 238):
                monster = 26
                if monster == 25 or monster == 26 or monster == 27:
                    if dice == 1 or dice == 3 or dice == 5:
    #             textAlign(CENTER)
    #             text("Void Essence", width /2, height - 200)
                        inventory.Void_Essence = inventory.Void_Essence + 1
                    elif dice == 2 or dice == 4:
        #             textAlign(CENTER)
    #             text("Void Essence x2", width /2, height - 200)
                        inventory.Void_Essence = inventory.Void_Essence + 2
                    else:
    #             textAlign(CENTER)
    #             text("Void Essence x3", width /2, height - 200)
                        inventory.Void_Essence = inventory.Void_Essence + 3
            if isMouseWithinSpace(450, 650, 172, 238):
                monster = 27
                if monster == 25 or monster == 26 or monster == 27:
                    if dice == 1 or dice == 3 or dice == 5:
    #             textAlign(CENTER)
    #             text("Void Essence", width /2, height - 200)
                        inventory.Void_Essence = inventory.Void_Essence + 1
                    elif dice == 2 or dice == 4:
        #             textAlign(CENTER)
    #             text("Void Essence x2", width /2, height - 200)
                        inventory.Void_Essence = inventory.Void_Essence + 2
                    else:
    #             textAlign(CENTER)
    #             text("Void Essence x3", width /2, height - 200)
                        inventory.Void_Essence = inventory.Void_Essence + 3
            if isMouseWithinSpace(650, 650, 172, 238):
                monster = 28
            
        
            if monster == 16: #SPECIAL - double damage on all cards (READY)
                M_energy = 20
                M_health = 200
                M_charge = 15
                M_gain = 10
                M_name = "Golden Scarab"
            
            if monster == 17: #SPECIAL - double block on all block cards (READY)
                M_energy = 20
                M_health = 200
                M_charge = 15
                M_gain = 10
                M_name = "Mummy"
            
            if monster == 18: #SPECIAL - double damage on all cards (READY)
                M_energy = 20
                M_health = 250
                M_charge = 15
                M_gain = 10
                M_name = "Ancient Skeleton"
            
            if monster == 19: #SPECIAL - double damage on poison and corruption cards (READY)
                M_energy = 20
                M_health = 250
                M_charge = 15
                M_gain = 10
                M_name = "Giant Scorpion"
                
            if monster == 20: #SPECIAL - double damage on corruption cards (READY)
                M_energy = 20
                M_health = 400
                M_charge = 15
                M_gain = 10
                M_name = "Basilisk"
                
            if monster == 21: #SPECIAL - double effects on all cards (READY)
                M_energy = 20
                M_health = 220
                M_charge = 15
                M_gain = 10
                M_name = "Lava Slime"
                
            if monster == 22: #SPECIAL - double effects on all cards (READY)
                M_energy = 30
                M_health = 330
                M_charge = 15
                M_gain = 10
                M_name = "Lava Golem"
            
            if monster == 23: #SPECIAL - double effects on all cards (READY)
                M_energy = 20
                M_health = 280
                M_charge = 15
                M_gain = 10
                M_name = "Fire Drake"
                
            if monster == 24: #SPECIAL - tripple effects on all cards (READY)
                M_energy = 20
                M_health = 600
                M_charge = 15
                M_gain = 10
                M_name = "Crimson Dragon"
                
            if monster == 25: #SPECIAL - tripple effects on all cards (READY)
                M_energy = 20
                M_health = 450
                M_charge = 15
                M_gain = 10
                M_name = "Voidling"
            
            if monster == 26: #SPECIAL - quad effects on all cards (READY)
                M_energy = 20
                M_health = 600
                M_charge = 15
                M_gain = 10
                M_name = "Void Elemental"
            
            if monster == 27: #SPECIAL - attack cards do 10x damage (READY)
                M_energy = 20
                M_health = 150
                M_charge = 15
                M_gain = 10
                M_name = "Void Tentacle"
            
            if monster == 28: #SPECIAL - quad damage on all cards, +40 damage to attack cards, immune to piercing (READY)
                M_energy = 50
                M_health = 3000
                M_charge = 25
                M_gain = 20
                M_name = "DeathGazer"
                
                
def endOfCombat():
    if (M_health == 0):
        screen = "Map"
        return screen
                
            
            
