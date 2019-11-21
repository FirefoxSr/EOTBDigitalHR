import json
jsonfile = open('encountertable.json')
encounter = json.load(jsonfile)
print(encounter)
square = input('What square did you land on? ')
Area = input('What area are you in? ')
num = input('enter your dice roll here: ')
print('Hallo')


print(num)
print(encounter)
print(encounter["EncounterTable"][Area][square]["Dice" + num])