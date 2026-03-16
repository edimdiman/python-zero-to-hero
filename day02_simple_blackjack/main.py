# a super simple blackjack game will live here

import secrets 

player_score = 0
pc_score = 0

while True: 
    pc_upcard = secrets.choice(range(1,12))
    pc_downcard = secrets.choice(range(1,12))
    player_upcard = secrets.choice(range(1,12))

    if pc_upcard >= 10: 
        # add insurance later
        if pc_downcard == 11:
            # add cool spinning or dot animation here eventually, seems too 
            # complicated at the moment
            print("Dealer has a blackjack, better luck next time")
            break
        else:
            print("Nobody is home, game goes on")


            

