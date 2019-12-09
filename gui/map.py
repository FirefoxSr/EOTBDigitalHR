def setup():
    global map
    fullScreen()
    map = loadImage("map.png")

def draw():
    global map
    background(0);
    image(map,0,0)
