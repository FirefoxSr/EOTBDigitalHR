import Encounters
import json

def playerTurn(n):
    global endTurn
    if (endTurn == True):
        if (n == 1):
            n = 2
        elif (n == 2):
            n = 1
        return n
    
    
endTurn = False

def setup():
    global mapImage, enemy, currentPlayer, p1Image, p2Image, debugImg, endTurn, currentPlayer, img
    fullScreen()
    mapImage = loadImage("map.png")
    p1Image = loadImage("p1.png")
    p2Image = loadImage("p2.png")
    imageMode(CENTER)
    textSize(40)
    ellipseMode(CENTER)
    enemy = ''
    currentPlayer = 1
def draw():
    global mapImage, enemy, playerImage, endTurn, currentPlayer, p1Image, p2Image
    background(0)
    image(mapImage, 400, height // 2)
    message = 'Please click on the square you landed.'
    text(message, 800, 200)
    text(str(enemy),800,700)
    text("Go to combat",1500, 976)
    text("Open Crafting",800, 976)
    text("Current Player: " + str(currentPlayer),805,240)

    
def isMouseWithinSpace(x,y,w,h):
        if (x < mouseX < x + w and y < mouseY < y + h):
            return True
        else:
            return False


def mouseClicked():
    global enemy, currentPlayer, p1Image, p2Image, playerImage, endTurn, currentPlayer
    #this calls the function to move on to the next player
    if isMouseWithinSpace(1488,931,186,58):
        endTurn = True
        currentPlayer = playerTurn(currentPlayer)
    
    #here we execute a function if the user clicks on squares on the map, this is gona be a long one. Just bear with me ^^
    #area 1
    if isMouseWithinSpace(132,933,32,228):
        enemy = Encounters.encounter(1)
        playerImage(currentPlayer)
    if isMouseWithinSpace(167,951,31,28):
        enemy = Encounters.encounter(1)
    if isMouseWithinSpace(184,912,31,30):
        enemy = Encounters.encounter(1)
    if isMouseWithinSpace(138,894,32,29):
        enemy = Encounters.encounter(1)
    if isMouseWithinSpace(286,883,31,29):
        enemy = Encounters.encounter(1)
    if isMouseWithinSpace(234,896,31,29):
        enemy = Encounters.encounter(1)
    #area 2
    if isMouseWithinSpace(245,862,32,29):
        enemy = Encounters.encounter(2)
    if isMouseWithinSpace(268,946,32,29):
        enemy = Encounters.encounter(2)
    if isMouseWithinSpace(319,918,31,29):
        enemy = Encounters.encounter(2)
    if isMouseWithinSpace(357,951,31,29):
        enemy = Encounters.encounter(2)
    if isMouseWithinSpace(351,880,31,29):
        enemy = Encounters.encounter(2)
    if isMouseWithinSpace(414,886,31,29):
        enemy = Encounters.encounter(2)
    #area 3
    if isMouseWithinSpace(433,939,31,29):
        enemy = Encounters.encounter(3)
    if isMouseWithinSpace(553,882,31,29):
        enemy = Encounters.encounter(3)
    if isMouseWithinSpace(613,886,31,29):
        enemy = Encounters.encounter(3)
    if isMouseWithinSpace(659,918,31,29):
        enemy = Encounters.encounter(3)
    #area 4
    if isMouseWithinSpace(583,926,31,29):
        enemy = Encounters.encounter(4)
    if isMouseWithinSpace(601,857,31,29):
        enemy = Encounters.encounter(4)
    if isMouseWithinSpace(630,810,31,29):
        enemy = Encounters.encounter(4)
    #area 5
    if isMouseWithinSpace(619,760,31,29):
        enemy = Encounters.encounter(5)
    if isMouseWithinSpace(646,720,31,29):
        enemy = Encounters.encounter(5)
    if isMouseWithinSpace(574,723,31,29):
        enemy = Encounters.encounter(5)
    #area 6
    if isMouseWithinSpace(675,681,31,29):
        enemy = Encounters.encounter(6)
    if isMouseWithinSpace(655,636,31,29):
        enemy = Encounters.encounter(6)
    if isMouseWithinSpace(591,646,31,29):
        enemy = Encounters.encounter(6)
    if isMouseWithinSpace(550,748,31,29):
        enemy = Encounters.encounter(6)
    #area 7
    if isMouseWithinSpace(509,705,31,29):
        enemy = Encounters.encounter(7)
    if isMouseWithinSpace(512,742,31,29):
        enemy = Encounters.encounter(7)
    if isMouseWithinSpace(526,698,31,29):
        enemy = Encounters.encounter(7)
    if isMouseWithinSpace(554,648,31,29):
        enemy = Encounters.encounter(7)
    if isMouseWithinSpace(546,605,31,29):
        enemy = Encounters.encounter(7)
    if isMouseWithinSpace(601,588,31,29):
        enemy = Encounters.encounter(7)
    #area 8
    if isMouseWithinSpace(452,759,31,29):
        enemy = Encounters.encounter(8)
    if isMouseWithinSpace(475,691,31,29):
        enemy = Encounters.encounter(8)
    if isMouseWithinSpace(501,638,31,29):
        enemy = Encounters.encounter(8)
    #area 9
    if isMouseWithinSpace(441,624,31,29):
        enemy = Encounters.encounter(9)
    if isMouseWithinSpace(413,682,31,29):
        enemy = Encounters.encounter(9)
    if isMouseWithinSpace(321,743,31,29):
        enemy = Encounters.encounter(9)
    if isMouseWithinSpace(267,765,31,29):
        enemy = Encounters.encounter(9)
    if isMouseWithinSpace(204,774,31,29):
        enemy = Encounters.encounter(9)
    #area 10
    if isMouseWithinSpace(377,750,31,29):
        enemy = Encounters.encounter(10)
    if isMouseWithinSpace(322,698,31,29):
        enemy = Encounters.encounter(10)
    if isMouseWithinSpace(266,680,31,29):
        enemy = Encounters.encounter(10)
    if isMouseWithinSpace(243,733,31,29):
        enemy = Encounters.encounter(10)
    if isMouseWithinSpace(205,699,31,29):
        enemy = Encounters.encounter(10)
    if isMouseWithinSpace(170,737,31,29):
        enemy = Encounters.encounter(10)
    #area 11
    if isMouseWithinSpace(380,653,31,29):
        enemy = Encounters.encounter(11)
    if isMouseWithinSpace(293,621,31,29):
        enemy = Encounters.encounter(11)
    if isMouseWithinSpace(157,650,31,29):
        enemy = Encounters.encounter(11)
    if isMouseWithinSpace(99,746,31,29):
        enemy = Encounters.encounter(11)
    if isMouseWithinSpace(93,679,31,29):
        enemy = Encounters.encounter(11)
    #area 12
    if isMouseWithinSpace(362,600,31,29):
        enemy = Encounters.encounter(12)
    #area 13
    if isMouseWithinSpace(125,600,31,29):
        enemy = Encounters.encounter(13)
    if isMouseWithinSpace(112,499,31,29):
        enemy = Encounters.encounter(13)
    if isMouseWithinSpace(97,412,31,29):
        enemy = Encounters.encounter(13)
    if isMouseWithinSpace(134,388,31,29):
        enemy = Encounters.encounter(13)
    if isMouseWithinSpace(131,296,31,29):
        enemy = Encounters.encounter(13)
    if isMouseWithinSpace(218,305,31,29):
        enemy = Encounters.encounter(13)
    #area 14
    if isMouseWithinSpace(288,301,31,29):
        enemy = Encounters.encounter(14)
    if isMouseWithinSpace(421,293,31,29):
        enemy = Encounters.encounter(14)
    if isMouseWithinSpace(549,287,31,29):
        enemy = Encounters.encounter(14)
    if isMouseWithinSpace(533,329,31,29):
        enemy = Encounters.encounter(14)
    if isMouseWithinSpace(596,350,31,29):
        enemy = Encounters.encounter(14)
    if isMouseWithinSpace(630,367,31,29):
        enemy = Encounters.encounter(14)
    if isMouseWithinSpace(670,344,31,29):
        enemy = Encounters.encounter(14)
    if isMouseWithinSpace(659,457,31,29):
        enemy = Encounters.encounter(14)
    #area 15
    if isMouseWithinSpace(670,515,31,29):
        enemy = Encounters.encounter(15)
    #area 16
    if isMouseWithinSpace(588,500,31,29):
        enemy = Encounters.encounter(16)
    if isMouseWithinSpace(547,471,31,29):
        enemy = Encounters.encounter(16)
    #area 17
    if isMouseWithinSpace(500,414,31,29):
        enemy = Encounters.encounter(17)
    if isMouseWithinSpace(471,385,31,29):
        enemy = Encounters.encounter(17)
    if isMouseWithinSpace(391,349,31,29):
        enemy = Encounters.encounter(17)
    if isMouseWithinSpace(342,348,31,29):
        enemy = Encounters.encounter(17)
    if isMouseWithinSpace(259,418,31,29):
        enemy = Encounters.encounter(17)
    #area 18
    if isMouseWithinSpace(161,533,31,29):
        enemy = Encounters.encounter(18)
    if isMouseWithinSpace(163,475,31,29):
        enemy = Encounters.encounter(18)
    if isMouseWithinSpace(231,387,31,29):
        enemy = Encounters.encounter(18)
    if isMouseWithinSpace(589,419,31,29):
        enemy = Encounters.encounter(18)
    if isMouseWithinSpace(230,461,31,29):
        enemy = Encounters.encounter(18)
    if isMouseWithinSpace(203,502,31,29):
        enemy = Encounters.encounter(18)
    if isMouseWithinSpace(269,525,31,29):
        enemy = Encounters.encounter(18)
    if isMouseWithinSpace(380,521,31,29):
        enemy = Encounters.encounter(18)
    if isMouseWithinSpace(436,538,31,29):
        enemy = Encounters.encounter(18)
    if isMouseWithinSpace(487,531,31,29):
        enemy = Encounters.encounter(18)
    if isMouseWithinSpace(474,481,31,29):
        enemy = Encounters.encounter(18)
    if isMouseWithinSpace(411,490,31,29):
        enemy = Encounters.encounter(18)
    #area 19
    if isMouseWithinSpace(364,473,31,29):
        enemy = Encounters.encounter(19)
    #area 20
    if isMouseWithinSpace(101,156,31,29):
        enemy = Encounters.encounter(20)
    if isMouseWithinSpace(154,108,31,29):
        enemy = Encounters.encounter(20)
    if isMouseWithinSpace(166,154,31,29):
        enemy = Encounters.encounter(20)
    if isMouseWithinSpace(300,153,31,29):
        enemy = Encounters.encounter(20)
    if isMouseWithinSpace(371,108,31,29):
        enemy = Encounters.encounter(20)
    #area 21
    if isMouseWithinSpace(227,128,31,29):
        enemy = Encounters.encounter(21)
    if isMouseWithinSpace(295,104,31,29):
        enemy = Encounters.encounter(21)
    if isMouseWithinSpace(380,158,31,29):
        enemy = Encounters.encounter(21)
    if isMouseWithinSpace(455,139,31,29):
        enemy = Encounters.encounter(21)
    if isMouseWithinSpace(516,148,46,43):
        enemy = Encounters.encounter(20)
    if isMouseWithinSpace(527,102,31,29):
        enemy = Encounters.encounter(20)
    #area 22 (final boss)
    if isMouseWithinSpace(597,107,77,65):
        enemy = Encounters.encounter(22)
