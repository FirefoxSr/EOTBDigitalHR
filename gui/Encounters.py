def encounters(x):
    
    squareCheck = 0
    
    while(squareCheck != 22):
        
        check = False
        #generate the random dice roll here
        num = str(random.randint(1, 6))
    
        #opens the json file and saves it to a variable
        jsonEcnounterTable = open('encountertable.json')
        encounter = json.load(jsonEcnounterTable)
        jsonMonsters= open('monsters.json')
        monsters = json.load(jsonMonsters)
        
        def draw():
            background(255)
    
       def switch(state):
        case 0:
            fill(0)
            text ("what square did you land on? \n"+result, 133, 333); 
            break
        
        case 1:
            fill(255, 2, 2); 
            text ("Thanks \n"+result, 133, 633); 
            break
    
        def keyPressed:
        
            if (key==ENTER||key==RETURN):
            
                state = state + 1
            else:
            result = result + key
        
        #asks the player to input the square they landed on and turns that integer into a string
        while (check == False):
            square = input('What square did you land on? ')
            squareCheck = int(square)
            square = 'playerSquare' + str(square)
            if (squareCheck > 22 or squareCheck == 0):
                check = False
                print('That square does not exist')
            else:
                check = True
                
    
        
    
        #saves the encountered enemy to a variable so the program can use it
        enemy = encounter["EncounterTable"][square]["Dice" + num]
        
        #prints the encounter to the console
        print(encounter["EncounterTable"][square]["Dice" + num])
    
        
        #this gets the enemy stats out of the json file
    
        enemyStats = monsters["monsters"][enemy]
        if (enemyStats == "No_Encounter"):
            print('You didn\'t encounter any enemies')
        else:
            startingEnergy = monsters["monsters"][enemy]["starting_energy"]
            print(startingEnergy + ' starting energy')
            usingCards = monsters["monsters"][enemy]["using_cards"]
            print(usingCards + ' using cards')
            charging = monsters["monsters"][enemy]["charging"]
            print(charging + ' charging')
            special = monsters["monsters"][enemy]["special"]
            print(special)
    
        
    
        if (squareCheck == 22):
            programStop = input('Do you want to quit? y/n: ')
            if (programStop == 'y'):
                squareCheck = 22
            else:
                squareCheck = 0
