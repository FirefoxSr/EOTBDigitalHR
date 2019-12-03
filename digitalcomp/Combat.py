def combat():
        font = createFont('Arial', 32)
        turn = 0
        P_energy = 100
        P_health = 1000
        P_block = 100
        P_corruption = 0
        P_poison = 0
        P_fire = 0
        M_energy = 100
        M_health = 1000
        M_block = 100
        M_corruption = 0
        M_poison = 0
        M_fire = 0
        damage = 0
        block = 0
        piercing = 0
        corruption = 0
        poison = 0
        fire = 0
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
        background(0,0,0)
        textFont(font)
        fill(256,256,256)
        textSize(50)
        textAlign(CENTER)
        
        text('Player', 1650, 100)
        text('Monster', 1650, 200)
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
        
        text('Monster Corruption: ' + str(M_corruption), 1650, 650)
        text('Player Corruption: ' + str(P_corruption), 1650, 700)
        text('Monster Poison: ' + str(M_poison), 1650, 750)
        text('Player Poison: ' + str(P_poison), 1650, 800)
        text('Monster Fire: ' + str(M_fire), 1650, 850)
        text('Player Fire: ' + str(P_fire), 1650, 900)
        
        text('Reset', 250, 1000)
        
        image(img_attack_5, 50, 300)
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
        
        def isMouseWithinSpace(x,y,w,h):
            if (x < mouseX < x + w and y < mouseY < y + h):
                return True
            else:
                return False 
        
        def mousePressed():
        global M_health, M_block, M_corruption, M_poison, M_fire, P_health, P_block, P_corruption, P_poison, P_fire, corruption, poison, damage, fire, block, turn, piercing
        if isMouseWithinSpace(1550, 50, 200, 50):
        turn = 1
        if isMouseWithinSpace(1550, 150, 200, 50):
        turn = 2
        
        if isMouseWithinSpace(150, 950, 200, 50):
        damage = 0
        block = 0
        piercing = 0
        corruption = 0
        poison = 0
        fire = 0
        
        if isMouseWithinSpace(50, 300, 172, 238):
        damage = damage + 5
        if isMouseWithinSpace(250, 300, 172, 238):
        damage = damage + 8
        if isMouseWithinSpace(450, 300, 172, 238):
        block = block + 5
        if isMouseWithinSpace(650, 300, 172, 238):
        block = block + 10
        if isMouseWithinSpace(850, 300, 172, 238):
        piercing = piercing + 5
        if isMouseWithinSpace(50, 600, 172, 238):
        corruption = corruption + 1
        if isMouseWithinSpace(850, 600, 172, 238):
        poison = poison + 1
        if isMouseWithinSpace(250, 600, 172, 238):
        damage = damage + 5
        fire = fire + 1
        
        #Dit is voor de End Turn
        if isMouseWithinSpace(1550, 1000, 200, 50):
        if turn == 1:
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
        P_block = P_block + block
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
        
        if  turn == 2:
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
        
        P_block = P_block - damage
        P_health = M_health - piercing
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
