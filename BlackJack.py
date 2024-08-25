# BlackJack

import random
import sys
 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_cards = []
computers_cards = []

play_on = True

for i in range(2):
    random_card_index = random.randint(0, len(cards)-1)
    random_card_index_comp = random.randint(0, len(cards)-1)
    players_cards.append(cards[random_card_index])
    computers_cards.append(cards[random_card_index_comp])
    
def Ace(hand):
    """Enter the player's cards to check for Ace rule"""
    if 11 in hand:
        if sum(hand) > 21:
            for value in range(len(hand)):
                if hand[value] == 11:
                    hand[value] = 1
    
def BlackJack(p_sum):
    if p_sum == 21:
        print("You Lose, The opponent has a BlackJack")
        sys.exit()
        

play = input("Do you want to play Black Jack, Type 'y' for yes or 'n' for no: ").lower()
if play == 'y':
    print("""
                      .------.
         .------.           |A .   |
         |A_  _ |    .------; / \  |
         |( \/ )|-----. _   |(_,_) |
         | \  / | /\  |( )  |  I  A|
         |  \/ A|/  \ |_x_) |------'
         `-----+'\  / | Y  A|
               |  \/ A|-----'    hjw
               `------'
          """)
    print(f'Your current hand: {players_cards}, Your current score: {sum(players_cards)}')
    print(f"Computer's current hand: [{computers_cards[0]}], Computer's current score: {computers_cards[0]}\n")
    BlackJack(sum(players_cards))
    while play_on:
        proceed = input("Type 'y' to get another card, or 'n' to pass: ")
        print("\n")
        if proceed == 'y':
            players_cards.append(cards[random.randint(0, len(cards)-1)])
            print(f"Your current hand: {players_cards}, Your current score: {sum(players_cards)}")
            print(f"Computer's current hand: [{computers_cards[0]}],Computer's current score: {computers_cards[0]} \n")
            if sum(players_cards) > 21:
                print("You Busted!")
                print("You Lose")
                play_on = False
           
        elif proceed == 'n':
            print(f"Your current hand: {players_cards}, Your current score: {sum(players_cards)}")
            print(f"Computers current hand: {computers_cards}, Computer's current: {sum(computers_cards)}\n")
                      
            Ace(players_cards)
            Ace(computers_cards)
            
            players_sum = sum(players_cards)
            computers_sum = sum(computers_cards)
        
            BlackJack(computers_sum)
            
            if computers_sum <= 16:
                print("Computer will draw a 3rd hand")
                computers_cards.append(cards[random.randint(0, len(cards)-1)])
                print(f"Your final hand: {players_cards}, Your final score: {sum(players_cards)}")
                print(f"Computer's final hand: {computers_cards}, Computer's final score: {sum(computers_cards)}\n")
                computers_sum = sum(computers_cards)
                if computers_sum >21:
                    print("Computer is Busted!\nYou Win")
                elif players_sum > computers_sum:
                    print("You Win")
                elif players_sum < computers_sum:
                    print("You Lose")
                elif players_sum == computers_sum:
                    print("It's a Draw")
                play_on = False
            else:
                if computers_sum >21:
                    print("Computer is Busted!\nYou Win")
                elif players_sum > computers_sum:
                    print("You Win")
                elif players_sum < computers_sum:
                    print("You Lose")
                elif players_sum == computers_sum:
                    print("It's a Draw")
                play_on = False

else:
    sys.exit()
    
#If it is a ace it can be 1 or 11 - Theory of blackJack
#Sum of 21 is allowed
#If the sum of direct first two cards of a players is = 21 then that player is said to have BlackJack and he wins










