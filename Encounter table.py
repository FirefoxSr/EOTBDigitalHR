squareCheck = 0

while (squareCheck != 22):
    import json
    import random

    check = False
    #generate the random dice roll here
    num = str(random.randint(1, 6))

    #opens the json file and saves it to a variable
    jsonfile = open('encountertable.json')
    encounter = json.load(jsonfile)

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

    if (squareCheck == 22):
        programStop = input('Do you want to quit? y/n: ')
        if (programStop == 'y'):
            squareCheck = 22
        else:
            squareCheck = 0
