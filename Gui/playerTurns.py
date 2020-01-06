def playerTurn(n):
    if (n == 2):
        n = 1
    elif (n == 1):
        n = 2
    return n
turn = playerTurn(1)
print(turn)
nextTurn = True
if (nextTurn == True):
    playerTurn(turn)
