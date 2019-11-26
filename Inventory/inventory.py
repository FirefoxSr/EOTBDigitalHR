#a set of monsters in a set
Monster_set = {"Slime", "Bear", "Wolf", "Skeleton", "Treant", "Arcane Wolf", "Fairy",
"Mana Golem", "Skeleton Mage", "Void Spawn", "Ghost", "Zombie", "Haunter", "Haunted Tree", "Grim Reaper", 
"Golden Scarab", "Ancient Skeleton", "Giant Scorpion", "Basilisk"}

import json
import random

#random dice roll
min = 1 
max = 6
num = (random.randint(min,max))

#opens a json file with the monsters drop in it
json_Iventory = open('inventory.json')
iventory = json.load(json_Iventory)

#ask the user the name of the monster
Monster = (input("What is the name of the monster? "))


if num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6:
    if Monster in Monster_set:
        item = iventory["MonsterDrop"][Monster]["Dice" + str(num)]
        print(iventory["MonsterDrop"][Monster]["Dice" + str(num)])
    else:
        print("<unvalid name>")







