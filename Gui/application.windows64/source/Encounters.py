def encounter(x):
    import json
    import random
    #generate the random dice roll here
    num = str(random.randint(1, 6))

    #opens the json file and saves it to a variable
    jsonEcnounterTable = open('data/encounterTable.json')
    encounter = json.load(jsonEcnounterTable)
    jsonMonsters= open('data/monsters.json')
    monsters = json.load(jsonMonsters)

    square = x
    square = 'playerSquare' + str(square)


    

    #saves the encountered enemy to a variable so the program can use it
    enemy = encounter["EncounterTable"][square]["Dice" + num]
    
    #prints the encounter to the console
    print(encounter["EncounterTable"][square]["Dice" + num])

    
    #this gets the enemy stats out of the json file

    enemyStats = monsters["monsters"][enemy]
    if (enemyStats == "No_Encounter"):
        message = "You didn't encounter any enemies."
    else:
        startingEnergy = monsters["monsters"][enemy]["starting_energy"]
        print(startingEnergy + ' starting energy')
        usingCards = monsters["monsters"][enemy]["using_cards"]
        print(usingCards + ' using cards')
        charging = monsters["monsters"][enemy]["charging"]
        print(charging + ' charging')
        special = monsters["monsters"][enemy]["special"]
        print(special)

    return enemy
    
