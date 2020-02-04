import cards
from Map import mouseClicked
import Map
import playerTurns
import backgroundScroll
screen = 'combat'

def setup():
    global img_Lillie, img_Kriv, img_error, img_empty, monsterTest, psn, screen, monster_img, poisonCountPlayer, poisonCountMonster, corruptionCountPlayer, corruptionCountMonster, turnCount, corruptionIsPlayed, poisonIsPlayed, img_Slime, img_Wolf, img_Skeleton, img_Treant, img_Fairy, img_Arcanewolf, img_SkeletonMage, img_ManaGolem, img_VoidSpawn, img_Ghost, img_Zombie, img_HauntedTree, img_GrimReaper, img_GoldenScarab, img_Mummy, img_AncientSkeleton, img_GiantScorpion, img_Basilisk, img_LavaGolem, img_FireDrake, img_CrimsonDragon, img_Voidling, img_VoidElemental, img_VoidTentacle, img_DeathGazer
    fullScreen()
    background(0)
    textSize(50)
    imageMode(CORNER)
    img_empty = ('empty.png')
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
    img_Lillie = loadImage('Lillie of the Valley.png')
    img_Kriv = loadImage('KrivVaati.png')
    monsterTest = loadImage('fairy.png')
    img_error = loadImage('Error.png')
    psn = loadImage('psn.png')
    cor = loadImage('cor.png')
    brn = loadImage('brn.png')
    screen = 'combat'
    turn = 'player'
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
    global img_Lillie, player_img, img_Kriv, monsterTest, psn, screen, monster_img, poisonCountPlayer, poisonCountMonster, corruptionCountPlayer, corruptionCountMonster, poisonIsPlayed, corruptionIsPlayed, img_Slime
    #all the display stuff for the player
    print(Map.currentPlayer)
    playerImg = ''
    if Map.currentPlayer == 1:
        currentPlayer = 1
        playerImg = img_Lillie
    if Map.currentPlayer == 2:
        currentPlayer = 2
        playerImg = img_Kriv
    imageMode(CORNER)
    image(playerImg, 150, 600, width // 6, height // 3)
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
    monster_img = monsterImg()
    print(enemy)
    if Map.enemy == 'No_Encounter':
        screen = 'No_Encounter'
        background(0)
        textSize(100)
        text('You didn\'t encounter any monster', width // 8, height // 2)
    else:
        backgroundScroll.draw()
        imageMode(CORNER)
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
        text('Choose attack', 500, 1020)
        text('End Turn', 900, 1020)
        text('Back to map', 100, 1020)
        noFill()
        stroke(255)
        rectMode(CORNER)
        rect(495, 970, 350, 60)
        rect(890, 970, 235, 60)
        rect(95, 970, 305, 60)
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
    if isMouseWithinSpace(495, 970, 350, 60):
        screen = 'cards'
    if isMouseWithinSpace(895, 970, 235, 60):
        endTurn = True


def monsterImg():
    global enemy, img_error, img_empty, img_Slime, img_Wolf, img_Skeleton, img_Treant, img_Fairy, img_ArcaneWolf, img_SkeletonMage, img_ManaGolem, img_VoidSpawn, img_Ghost, img_Zombie, img_HauntedTree, img_GrimReaper, img_GoldenScarab, img_Mummy, img_AncientSkeleton, img_GiantScorpion, img_Basilisk, img_LavaGolem, img_FireDrake, img_CrimsonDragon, img_Voidling, img_VoidElemental, img_VoidTentacle, img_DeathGazer
    monsterImg = ''
    enemy = Map.enemy
    if enemy == 'Slime':
        monsterImg = img_Slime
        return monsterImg
    if enemy == 'Wolf':
        monsterImg = img_Wolf
        return monsterImg
    if enemy == 'Skeleton':
        monsterImg = img_Skeleton
        return monsterImg
    if enemy == 'Treant':
        monsterImg = img_Treant
        return monsterImg
    if enemy == 'Fairy':
        monsterImg = img_Fairy
        return monsterImg
    if enemy == 'ArcaneWolf':
        monsterImg = img_ArcaneWolf
        return monsterImg
    if enemy == 'SkeletonMage':
        monsterImg = img_SkeletonMage
        return monsterImg
    if enemy == 'ManaGolem':
        monsterImg = img_ManaGolem
        return monsterImg
    if enemy == 'VoidSpawn':
        monsterImg = img_voidSpawn
        return monsterImg
    if enemy == 'Ghost':
        monsterImg = img_Ghost
        return monsterImg
    if enemy == 'Zombie':
        monsterImg = img_Zombie
        return monsterImg
    if enemy == 'HauntedTree':
        monsterImg = img_GrimReaper
        return monsterImg
    if enemy == 'GoldenScarab':
        monsterImg = img_GoldenScarab
        return monsterImg
    if enemy == 'Mummy':
        monsterImg = img_Mummy
        return monsterImg
    if enemy == 'AncientSkeleton':
        monsterImg = img_AncientSkeleton
        return monsterImg
    if enemy == 'GiantScorpion':
        monsterImg = img_GiantScorpion
        return monsterImg
    if enemy == 'Basilisk':
        monsterImg = img_Basilisk
        return monsterImg
    if enemy == 'LavaGolem':
        monsterImg = img_LavaGolem
        return monsterImg
    if enemy == 'FireDrake':
        monsterImg = img_fireDrake
        return monsterImg
    if enemy == 'CrimsonDragon':
        monsterImg = img_CrimsonDragon
        return monsterImg
    if enemy == 'Voidling':
        monsterImg = img_Voidling
        return monsterImg
    if enemy == 'VoidElemental':
        monsterImg = img_VoidElemental
        return monsterImg
    if enemy == 'VoidTentacle':
        monsterImg = img_VoidTentacle
        return monsterImg
    if enemy == 'DeathGazer':
        monsterImg = img_DeathGazer
        return monster_img
    if enemy == 'No_Encounter':
        monsterImg = img_empty
        
    else:
        monsterImg = img_error
        
    return monsterImg

        
        
    

        
