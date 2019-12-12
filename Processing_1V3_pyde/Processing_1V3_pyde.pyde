def setup():
 fullScreen()
 global font, Scene, turn, dice, P_turn, M_turn, P_energy, P_health, P_block, M_energy, M_health, M_block, M_corruption, M_poison, M_fire, M_name, P_poison, P_corruption, P_fire, monster, energy, charging, P_gain, M_gain, M_charge, P_charge, damage, block, piercing, corruption, poison, fire, cleanse, heal, img_VoidSpawn, img_ManaGolem, img_SkeletonMage, img_ArcaneWolf, img_fairy, img_treant, img_skeleton, img_bear, img_wolf, img_slime, img_attack_5, img_attack_8, img_block_5, img_block_10, img_piercing, img_cleanse, img_corruption, img_fireball, img_heal, img_magic_missile, img_poison
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
 
 monster = 0
 
 
#Graphic stuff. Everything that has to be on the screen is here. 
def draw():
 global message, font, Scene, turn, drop, P_turn, M_turn, P_energy, P_health, P_block, M_energy, M_health, M_block, M_name, monster, energy, charging, damage, block, piercing, corruption, poison, fire, cleanse, heal, img_VoidSpawn, img_ManaGolem, img_SkeletonMage, img_fairy, img_treant, img_skeleton, img_bear, img_wolf, img_slime, img_attack_5, img_attack_8, img_block_5, img_block_10, img_piercing, img_cleanse, img_corruption, img_fireball, img_heal, img_magic_missile, img_poison
 if Scene == 0:  #scene 0 = combat page. Scene 1 = monster select page. Scene 2 = item drop page.
  background(0,0,0)
  textFont(font)
  fill(256,256,256)
  textSize(50)
  textAlign(CENTER)
  if turn == 0:
   P_turn = 0
   M_turn = 0

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
        else:
            textAlign(CENTER)
            text("Mana Essence x2", width /2, height - 200)
  if monster == 1:
        if dice in range(1, 7):
            textAlign(CENTER)
            text("Nothing", width /2, height -200)

  if monster == 2:
        if dice == 1 or dice == 3 or dice == 4:
            textAlign(CENTER)
            text("Wolf Skin", width /2, height - 200)
        elif dice == 2 or dice == 5:
            textAlign(CENTER)
            text("Nothing", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Wolf Skin x2", width /2, height - 200)
            
  if monster == 3:
        if dice == 1:
            textAlign(CENTER)
            text("Bear Skin", width /2, height - 200)
        elif dice == 2 or dice == 5:
            textAlign(CENTER)
            text("Nothing", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Bear Skin x2", width /2, height - 200)
            
  if monster == 4:
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
            
  if monster == 5:
        if dice == 3 or dice == 5:
            textAlign(CENTER)
            text("Wooden Chunk x3", width /2, height - 200)
        elif dice == 4 or dice == 6:
            textAlign(CENTER)
            text("Wooden Stick x3", width /2, height - 200)
        else:
            textAlign(CENTER)
            text("Wooden Stick", width /2, height - 200)

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
    M_health = M_health - piercing
    M_corruption = M_corruption + corruption + corruption + corruption + corruption
    M_poison = M_poison + poison + poison + poison + poison + poison
    M_fire = M_fire + fire + fire + fire
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
     damage = damage + 2
     P_poison = P_poison - 1
     if P_poison < 0:
      P_poison = 0
    if P_corruption > 0:
     damage = damage + 5
     P_corruption = P_corruption - 1
     if P_corruption < 0:
      P_corruption = 0
    if P_fire > 0:
     damage = damage + 1
     P_fire = P_fire - 1
     if P_fire < 0:
      P_fire = 0
    M_energy = M_energy - energy
    M_block = M_block + block
    M_health = M_health + heal * 15
    P_block = P_block - damage
    P_health = P_health - piercing
    P_corruption = P_corruption + corruption + corruption + corruption + corruption
    P_poison = P_poison + poison + poison + poison + poison + poison
    P_fire = P_fire + fire + fire + fire
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
   
  if isMouseWithinSpace(50, 50, 172, 238):
   monster = 1
  if isMouseWithinSpace(250, 50, 172, 238):
   monster = 2
  if isMouseWithinSpace(450, 50, 172, 238):
   monster = 3
  if isMouseWithinSpace(650, 50, 172, 238):
   monster = 4
  if isMouseWithinSpace(850, 50, 172, 238):
   monster = 5
  if isMouseWithinSpace(50, 350, 172, 238):
   monster = 6
  if isMouseWithinSpace(250, 350, 172, 238):
   monster = 7
  if isMouseWithinSpace(450, 350, 172, 238):
   monster = 8
  if isMouseWithinSpace(650, 350, 172, 238):
   monster = 9
  if isMouseWithinSpace(850, 350, 172, 238):
   monster = 10
   

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
   
  
   
 if Scene == 2:
  if isMouseWithinSpace(450, 950, 200, 50):
   Scene = 0
