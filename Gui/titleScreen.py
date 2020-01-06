
def setup():
  global img, x, y, screen
  #img = loadImage("backGround.png")
  x = 0
  y = 540

def draw():
    global screen, img, x, y
    #image(img, x, y)
    tint(175, 255)
    x = x - 1
    if x == -2560:
        x = 0
    
    fill(255)
    strokeWeight(3)
    stroke(0)
    text('EYE OF THE BEHOLDER', 350, 320)
    noFill()
    strokeWeight(5)
    
    if mouseWithinSpace(1000, 660, 608, 150):
        stroke(255)
    rect(1000, 660, 608, 150)
    fill(255)
    strokeWeight(0)
    stroke(0)
    text('        START....... IF YOU DARE', 1000, 750)
    
def mouseWithinSpace(x, y, w, h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
        
