button1X = 50
button2X = 170
button3X = 330


def setup():
  global img, x, y, font, screen, img1, img2, currentNumber
  img1 = loadImage('plus.png')
  img2 = loadImage('minus.png')
  x = 0
  y = 0
  currentNumber = 0

def draw():
    ## Dit is de achtergrond die door blijft rollen
    global screen, img1, img2
    frameRate(100)
    
    ## Deze geeft de tekst aan van de Amount Players
    textAlign(TOP,CENTER)
    fill(255)
    strokeWeight(3)
    stroke(0)
    text('NUMBER OF PLAYERS', 350, 200)
    noFill()
    strokeWeight(5)
    stroke(0)
    
    ## Dit is de Plus om kleur groen te geven
    image(img1, 445, 600, 100, 100)
    rect(445, 600, 100, 95)
    if mouseWithinSpace(445, 600, 100, 95):
        stroke(3, 255, 12)
        rect(445, 600, 100, 95)
        stroke(0)
        rect(710, 600, 100, 95)
    
    ## Dit is de Min om kleur rood te geven
    image(img2,  721, 640, 80, 15)
    rect(710, 600, 100, 95)
    if mouseWithinSpace(710, 600, 100, 95):
        stroke(255, 0, 0)
        rect(710, 600, 100, 95)
        stroke(0)
        rect(445, 600, 100, 95)
    
    ## NEXT KNOP HIGHLIGHTEN
    if mouseWithinSpace(1170, 660, 90, 50):
        stroke(255)
    rect(1170, 660, 90, 50)
    fill(255)
    strokeWeight(0)
    text('NEXT', 1190, 685)
    
    text(str(currentNumber), 620, 400)
    fill(155)
    
    ## VOOR HET VERHOGEN VAN AANTAL
def increaseNumberCurrent():
    global currentNumber
    if currentNumber < 4:
        currentNumber = currentNumber + 1
    
def decreaseNumberCurrent():
    global currentNumber
    if currentNumber <= 0:
        return
    currentNumber = currentNumber - 1
        

def mouseWithinSpace(x, y, w, h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
    
def mousePressed():
    if mouseWithinSpace(445, 600, 100, 10):
        increaseNumberCurrent()
