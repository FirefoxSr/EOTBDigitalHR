import cards
import Encounters
screen = ''
def setup():
    global Lillie, monsterTest, psn, screen, monster_img, poisonCountPlayer, poisonCountMonster, corruptionCountPlayer, corruptionCountMonster, turnCount, corruptionIsPlayed, poisonIsPlayed
    fullScreen()
    background(0)
    textSize(50)
    Lillie = loadImage('Lillie of the Valley.png')
    monsterTest = loadImage('fairy.png')
    psn = loadImage('psn.png')
    cor = loadImage('cor.png')
    brn = loadImage('brn.png')
    screen = 'combat'
    monster_img = monsterTest
    turn = 'player'
    img_Slime = loadImage("slime.png")
    img_Wolf = loadImage("Wolf.png")
    img_Bear = loadImage("Bear.png")
    img_Skeleton = loadImage("skeleton.png")
    img_Treant = loadImage("treant.png")
    img_Fairy = loadImage("fairy.png")
    img_ArcaneWolf = loadImage("ArWolf.png")
    img_SkeletonMage = loadImage("skelMage.png")
    img_ManaGolem = loadImage("Magolem.png")
    img_VoidSpawn = loadImage("voidSpawn.png")
    img_Ghost = loadImage("Ghost.png")
    img_Zombie = loadImage("zombie.png")
    img_Haunter = loadImage("haunter.png")
    img_HauntedTree = loadImage("Htree.png")
    img_GrimReaper = loadImage("Grimreap.png")
    img_GoldenScarab = loadImage("Golden Scarab.png")
    img_Mummy = loadImage("Mummy.png")
    img_AncientSkeleton = loadImage("SkeletonAncient.png")
    img_GiantScorpion = loadImage("Scorpion.png")
    img_Basilisk = loadImage("Basilisk.png")
    img_LavaSlime = loadImage("LavaSlime.png")
    img_LavaGolem = loadImage("LavaGolem.png")
    img_FireDrake = loadImage("FireDrake.png")
    img_CrimsonDragon = loadImage("CrimsonDragon.png")
    img_Voidling = loadImage("Voidling.png")
    img_VoidElemental = loadImage("VoidElemental.png")
    img_VoidTentacle = loadImage("VoidTentacle.png")
    img_DeathGazer = loadImage("DeathGazer.png")
    
    poisonCountPlayer = 1
    poisonCountMonster = 0
    corruptionCountPlayer = 0
    corruptionCountMonster = 0
    fireCountPlayer = 0
    fireCountMonster = 0
    poisonIsPlayed = False
    corruptionIsPlayed = False
    turnCounter = 0
    energyPlayer = 0
    energyMonster = 0
    blockPlayer = 0
    blockMonster = 0
    hpPlayer = 0
    hpMonster = 0
    
def poison():
    global playerDamage, monsterDamage, poisonCountPlayer, poisonCountMonster, poisonIsPlayed
    if poisonIsPlayed == True:
        if turn == 'player':
            poisonCountMonster = 5
        if turn == 'monster':
            poisonCountPlayer = 5
def corruption():
    global playerDamage, monsterDamage, corruptioCountPlayer, corruptionCountMonster, corruptionIsPlayed
    if corruptionIsPlayed == True:
        if turn == 'player':
            corruptionCountplayer = 4
        if turn == 'monster':
            corruptionCountMonster = 4

def turnCount():
    global turnCount
    if corruptionIsPlayed == True or poisonIsPlayed == True:
        if endTurn == True:
            turnCounter =+ 1
    
def draw():
    global Lillie, monsterTest, psn, screen, monster_img, poisonCountPlayer, poisonCountMonster, corruptionCountPlayer, corruptionCountMonster, poisonIsPlayed, corruptionIsPlayed
    monster = Encounters.encounter
    print(monster)
    
    #all the display stuff for the player
    image(Lillie, 150, 600, width // 6, height // 3)
    text('HP: 100', 500, 650)
    text('Block: 20', 500, 750)
    text('Status:', 750, 650)
    text('energy:', 500, 850)
    if poisonCountPlayer > 0:
        image(psn, 920, 620)
    if corruptionCountPlayer > 0:
        pass
    #The functions for the poison and corruption status effects
    poison()
    corruption()
    turnCount()
    
    #all the display stuf for the monster
    image(monster_img, 1500, 100, width // 6, height // 3)
    text('HP: 100', 900, 150)
    text('Block: 20', 900, 250)
    text('status:', 1150, 150)
    text('energy:', 900, 350)
    if poisonCountMonster > 0:
        image(psn, 0, 0)
    if corruptionCountMonster > 0:
        pass
    
    
    textMode(CORNER)
    text('Choose attack', 500, 1000)
    text('End Turn', 800, 1000)
    noFill()
    stroke(255)
    rectMode(CORNER)
    rect(495, 950, 350, 60)
    rect(795, 950, 300, 60)
    text('Selected card: ' + cards.selectedCardFunc(), 100, 100)
    
    if screen == 'cards':
        cards.setup()
        cards.mouseClicked()
        cards.isMouseWithinSpace
        cards.draw()
    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mouseClicked():
    global screen, endTurn
    if isMouseWithinSpace(495, 950, 650, 60):
        screen = 'cards'
    if isMouseWithinSpace(800, 800, 20, 20):
        endTurn = True

        
