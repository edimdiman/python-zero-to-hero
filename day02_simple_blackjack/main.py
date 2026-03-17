# a super simple blackjack game will live here

import secrets 

player_score = 0
pc_score = 0
player_bust = False
pc_bust = False

while True: 
    pc_upcard = secrets.choice(range(1,12))
    pc_downcard = secrets.choice(range(1,12))
    player_upcard = secrets.choice(range(1,12))
    player_downcard = secrets.choice(range(1,12))

    if pc_upcard >= 10: 
        print(f"Dealer has a {pc_upcard}, checking for dealer blackjack")
        # pause to "check" for blackjack
        # add insurance later
        if pc_downcard == 11:
            # add cool spinning or dot animation here eventually, seems too 
            # complicated at the moment
            print("Dealer has a blackjack, better luck next time")
            break

    print("Nobody is home, game goes on")
    player_score = player_upcard + player_downcard
    pc_score = pc_upcard + pc_downcard

    while True:
        print(f"You have {player_score}. The computer's upcard is {pc_downcard}'")
        player_move = input("Would you like to hit or stay? Press 1 for hit, press 2 for stay.")
        if player_move == "1":
            player_score += secrets.choice(range(1,12))
            if player_score > 21:
                print("You bust! Game is over.")
                player_bust = True
                break 
        else:
            break

    while pc_score < 17 and player_bust == False:
        new_card = secrets.choice(range(1, 12))
        pc_score += new_card
        print(f"Dealer drew a {new_card}. Dealer total is now {pc_score}")
    
    if pc_score > 21:
        print("The dealer busted! You won!")
        break
    
    if player_score > pc_score:
        print(f"You have {player_score}. The dealer has {pc_score}. You won!")
        break

    if pc_score > player_score: 
        print(f"You have {player_score}. The dealer has {pc_score}. You loss!")
        break




            

            

