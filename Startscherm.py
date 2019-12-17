import playerScherm

def setup():
  global img, x, y, font, screen
  size(1280,720)
  img = loadImage("Achtergrond.png")
  font = createFont("Curse of the Zombie.otf", 65)
  x = 0
  y = 0
  screen = 'Startscherm'

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
    text('EYE\n\n       OF THE\n\n               BEHOLDER', 390, 280)
    noFill()
    strokeWeight(5)
    stroke(0)
    
    if 995 < mouseX < 1245 and 635 < mouseY < 935:
        stroke(150)
    rect(1000, 660, 250, 50)
    
    textFont(font, 18)
    fill(255)
    strokeWeight(0)
    stroke(0)
    text('        START....... IF YOU DARE', 998, 685)
        