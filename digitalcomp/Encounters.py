def encounter(enc):
    global enemy, mainMenu
    import json
    import random
    squareCheck = 0
    
    
    #generate the random dice roll here
    num = str(random.randint(1, 6))
    
    #opens the json file and saves it to a variable
    jsonEcnounterTable = open('encountertable.json')
    encounter = json.load(jsonEcnounterTable)
    jsonMonsters= open('monsters.json')
    monsters = json.load(jsonMonsters)
    
    #asks the player to input the square they landed on and turns that integer into a string
    square = enc
    square = 'playerSquare' + str(square)
    
    if (square == "playerSquareNone" or square == "playerSquare"):
        mainMenu = True
        return mainMenu
    
    else:
        mainMenu = False
        #saves the encountered enemy to a variable so the program can use it
        enemy = encounter["EncounterTable"][square]["Dice" + num]
        
        #prints the encounter to the console
        print(encounter["EncounterTable"][square]["Dice" + num])
        
        
        #this gets the enemy stats out of the json file
        
        enemyStats = monsters["monsters"][enemy]
        if (enemyStats == "No_Encounter"):
            print('You didn\'t encounter any enemies')
            text("You didn't encounter any enemyies", 500, 300)
        else:
            startingEnergy = monsters["monsters"][enemy]["starting_energy"]
            print(startingEnergy + ' starting energy')
            usingCards = monsters["monsters"][enemy]["using_cards"]
            print(usingCards + ' using cards')
            charging = monsters["monsters"][enemy]["charging"]
            print(charging + ' charging')
            special = monsters["monsters"][enemy]["special"]
            print(special)
        
        return enemy, mainMenu
