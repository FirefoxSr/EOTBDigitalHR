import Combat_screen
import backgroundScroll
selectedCard = ''
def setup():
    global img_attack_5, img_attack_10, img_block_5, img_block_10, img_piercing, img_cleanse, img_corruption, img_fireball, img_heal, img_magic_missile, img_poison, selectedCard
    background(0)
    img_attack_5 = loadImage("Attack_5.png")
    img_attack_10 = loadImage("Attack_8.png")
    img_block_5 = loadImage("Block_5.png")
    img_block_10 = loadImage("Block_10.png")
    img_piercing = loadImage("Piercing.png")
    img_cleanse = loadImage("Cleanse.png")
    img_corruption = loadImage("Corruption.png")
    img_fireball = loadImage("Fireball.png")
    img_heal = loadImage("Heal.png")
    img_magic_missile = loadImage("Magic_Missile.png")
    img_poison = loadImage("Poison.png")
    textSize(50)
    
def draw():
    global img_attack_5, img_attack_10, img_block_5, img_block_10, img_piercing, img_cleanse, img_corruption, img_fireball, img_heal, img_magic_missile, img_poison, selectedCard
    backgroundScroll.draw()
    imageMode(CORNER)
    image(img_attack_5,150,130)
    image(img_attack_10, 390, 130)
    image(img_block_5,640, 130)
    image(img_block_10, 890, 130)
    image(img_piercing,150, 430)
    image(img_cleanse, 390, 430)
    image(img_corruption, 640, 430)
    image(img_fireball, 890, 430)
    image(img_heal, 150, 730)
    image(img_magic_missile, 390, 730)
    image(img_poison, 640, 730)
    
    
def mouseClicked():    
    global selectedCard
    if mouseClicked:
        if mouseButton == LEFT:
            if isMouseWithinSpace(150, 130, 172, 238):
                selectedCard = 'attack_5'
                screen = 'combat'
                Combat_screen.setup()
                Combat_screen.draw()
            if isMouseWithinSpace(390, 130, 172, 238):
                text('Attack 10', 900, 900)
                selectedCard = 'attack_10'
                Combat_screen.setup()
                Combat_screen.draw()
            if isMouseWithinSpace(640, 130, 172, 238):
                text('Block 5', 900, 900)
                selectedCard = 'block_5'
                Combat_screen.setup()
                Combat_screen.draw()
            if isMouseWithinSpace(890, 130, 172, 238):
                text('Block 10', 900, 900)
                selectedCard = 'block_10'
                Combat_screen.setup()
                Combat_screen.draw()
            if isMouseWithinSpace(150, 430, 172, 238):
                text('Piercing', 900, 900)
                selectedCard = 'piercing'
                Combat_screen.setup()
                Combat_screen.draw()
            if isMouseWithinSpace(390, 430, 172, 238):
                text('Cleanse', 900, 900)
                selectedCard = 'cleanse'
                Combat_screen.setup()
                Combat_screen.draw()
            if isMouseWithinSpace(640, 430, 172, 238):
                text('Corruption', 900, 900)
                selectedCard = 'corruption'
                Combat_screen.setup()
                Combat_screen.draw()
            if isMouseWithinSpace(890, 430, 172, 238):
                text('Fireball', 900, 900)
                selectedCard = 'fireball'
                Combat_screen.setup()
                Combat_screen.draw()
            if isMouseWithinSpace(150, 730, 172, 238):
                text('Heal', 900, 900)
                selectedCard = 'heal'
                Combat_screen.setup()
                Combat_screen.draw()
            if isMouseWithinSpace(390, 730, 172, 238):
                text('Magic Missile', 900, 900)
                selectedCard = 'magic_missile'
                Combat_screen.setup()
                Combat_screen.draw()
            if isMouseWithinSpace(640, 730, 172, 238):
                text('Poison', 900, 900)
                selectedCard = 'poison'
                Combat_screen.setup()
                Combat_screen.draw()
                
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
    
def selectedCardFunc():
    global selectedCard
    return selectedCard


    
