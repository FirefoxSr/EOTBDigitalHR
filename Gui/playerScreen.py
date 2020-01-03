def playerscreen():
    def setup():
        global player_names, player1, player2, img
        img = loadImage('background_gui.jpeg')
        background(img)
        player_names = ['Drerrie', 'woeshoem']
        player1 = player_names[0]
        player2 = player_names[1]

    def draw():
        global player_names, player1, player2, img
        text('player 1: %s' % (player1), 50, 50)
        text('player 2: %s' % (player2), 50, 100) 
