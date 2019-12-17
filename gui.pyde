import Combat
import mainmenu
import Encounters
import playerscreen
import inventory
import playerturn
import startscreen
import test
import mapenc
import random
from random import randint

def setup():
    fullScreen()
    font = createFont("Curse of the Zombie.otf", 65)

state = 0
Mainmenu = 1
combat = 2
Inventory = 3
Playerscreen = 4
encounters = 5
Mapenc = 6
Startscreen = 7
state = Startscreen

if state == combat:
    Combat.setup()
    Combat.draw()

elif state == Mainmenu:
    mainmenu.setup()
    mainmenu.draw()

elif state == Inventory:
    inventory.setup()
    inventory.draw()

elif state == Playerscreen:
    playerscreen.setup()
    playerscreen.draw()
    
elif state == encounters:
    Encounters.setup()
    Encounters.draw()
    
elif state == Mapenc:
    mapenc.setup()
    mapenc.draw()
    
elif state == Startscreen:
    startscreen.setup()
    startscreen.draw()
