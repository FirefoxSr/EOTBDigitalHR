import AmountOfPlayers
if AmountOfPlayers == 1:
    pass
def playerTurn(n):
    global a
    if n == 0:
        return False
    if (n == 2):
        n = 1
        a = n
    elif (n == 1):
        n = 2
        a = n
    return n
turn = playerTurn(1)
nextTurn = True
if (nextTurn == True):
    playerTurn(turn)
    
def retPlayer():
    global a
    return a 
    
