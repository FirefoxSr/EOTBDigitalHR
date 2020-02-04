from cards import mouseClicked
from cards import selectedCardFunc
from Combat_screen import setup
def setup():
    pass
    
def attack_5():
    damage = 5
    if turn == 'player':
        hpMonster = hpMonster - 5
    if turn == 'monster':
        hpPlayer = hpPlayer - 5
def attack_10():
    damage = 10
    if turn == 'player':
        hpMonster = hpMonster - 10
    if turn == 'monster':
        hpPlayer = hpPlayer - 19
def block_5():
    block = 5
    if turn == 'player':
        playerBlock = playerBlock + 5
    if turn == 'monster':
        monsterBlock = monsterBlock + 5
def block_10():
    block = 10
    if turn == 'player':
        playerBlock = playerBlock + 10
    if turn == 'monster':
        monsterBlock = monsterBlock + 10
def cleanse():
    if turn == 'player':
        poisonCountPlayer = 0
        corruptionCountPlayer = 0
        
    if turn == 'monster':
        poisonCountMonster = 0
        corruptionCountMonster = 0
        
def corruption():
    corruptionIsPlayed = True    
        
def fireball():
    fireBallIsPlayed == True
    
def heal():
    if turn == 'player':
        playerHp = playerHp + 15
    if turn == 'monster':
        monsterHp = monsterHp + 15
        
def magicMissile():
    magicDmg = 5
    if turn == 'player':
        hpMonster = hpMonster - 5
    if turn == 'monster':
        hpPlayer = hpPlayer - 5
def piercing_5():
    pierceDmg = 5
    if turn == 'player':
        hpMonster = hpMonster - 5
    if turn == 'monster':
        hpPlayer = hpPlayer - 5
def poison():
    poisonIsPlayed = True


def draw():
    if selectedCard == 'attack_5':
        attack_5()
    if selectedCard == 'attack_10':
        attack_10()
    if selectedCard == 'block_5':
        block_5()
    if selectedCard == 'block_10':
        block_10()
    if selectedCard == 'cleanse':    
        cleanse()
    if selectedCard == 'corruption':
        corruption()
    if selectedCard == 'fireball':
        fireball()
    if selectedCard == 'heal':
        heal()
    if selectedCard == 'magic_missile':
        magicMissile()
    if selectedCard == 'piercing':
        piercing_5()
    if selectedCard == 'poison':
        poison()
        
    
    
    
    
    
