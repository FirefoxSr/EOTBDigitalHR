def setup():
  global img, x, y, font, screen
  size(1280,720)
  img = loadImage("Achtergrond.png")
  font = createFont("Curse of the Zombie.otf", 56)
  x = 0
  y = 0
  screen = 'playerScherm'

def draw():
    global screen
    frameRate(100)
    global img, x, y, font
    image(img, x, y)
    tint(175, 255 )
    x = x - 1
    if x == -2560:
        x = 0
    
    
    textAlign(TOP,CENTER)
    textFont(font)
    fill(255)
    strokeWeight(3)
    stroke(0)
    text('AMOUNT OF PLAYERS', 380, 280)
    noFill()
    strokeWeight(5)
    stroke(0)
