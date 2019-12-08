#Een set met alle Monsters
Monster_set = {"Slime", "Bear", "Wolf", "Skeleton", "Treant", "Arcane Wolf", "Fairy",
"Mana Golem", "Skeleton Mage", "Void Spawn", "Ghost", "Zombie", "Haunter", "Haunted Tree", "Grim Reaper", 
"Golden Scarab", "Ancient Skeleton", "Giant Scorpion", "Basilisk"}

#Een set met alle Items
DropItem_set = {"Bear Skin", "Wolf Skin", "Iron Chunk", "Wooden Stick", "Soul of the Dead", "Wooden Chunk", 
"Enchanted Wolf Skin", "Mana Essence", "Obsidian", "Soul of the Dead", "Void Energy", "Haunted Spirit", "Cursed Wood", 
"Gold Ingot", "Scorpion Poison", "Fire Essence", "Void Energy"}

import json
import random

while True:
    #Dobbelsteen
    num = (random.randint(1,6))

    #Open de json file met MonsterDrop erin
    json_Iventory = open('inventory.json')
    iventory = json.load(json_Iventory)

    #Vraag de user wat die wil doen
    option = input("Press d for drop, Press i for inventory or type 'exit' to quit the game: ")

    #Als user 'exit' heeft getypd stop het programma
    if option == "exit":
        exit()

    #Als user op 'd' heb geclickd vraag het programma de naam van de Monster en kijk welke item erbij hoort
    elif option == "d":
        #Vraag user naam van de Monster
        Monster = (input("What is the name of the monster? "))
        if Monster in Monster_set:
            item = iventory["MonsterDrop"][Monster]["Dice" + str(num)]
            print(iventory["MonsterDrop"][Monster]["Dice" + str(num)]) 
        #Als de naam niet in de lijst zit print het programma dit
        else:
            print("<unvalid name>")

    #Als user op "i" click laat het programma de inventory zien
    elif option == "i":
        for i in DropItem_set:
            print(i)
    #Als je iets anders typd vraag het programma opnieuw    
    else:
        print("Please press d or p or Type 'exit' to quit the game")

    
















