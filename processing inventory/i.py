import iventory
tekst = ""
def setup():
    size(800, 800)
    
def draw():
    background(0)
    text(tekst, 400, 400)
    
def keyPressed():
    global tekst
    tekst = tekst + key
    if (key == ENTER):
        tekst = ""
    
