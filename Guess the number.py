
import random
import sys

print("""
    ____                       _   _                                  _               
  / ____|                     | | | |                                | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                      
           """)                                                                           
print("Welcome to the Number Guessing game")
print("Hmm.. I'am guessing of a number between 1 to 100")
level = input('Do you want to play "easy" or "hard" level: ').lower()

actual_number = random.randint(1,100)
#print(f"Actual number = {actual_number}")
if level == "easy":
    guesses = 10
elif level == "hard":
    guesses = 5
    
while True:
    for i in range(0, guesses):
        print(f"You have {guesses} attempts remaining")
        player_guess = int(input("Make a guess: "))
        if player_guess < actual_number:
            print("Too Low")
        elif player_guess > actual_number:
            print("Too High")
        elif player_guess == actual_number:
            print("You got it!")
            print(f"The correct guess is {actual_number}")        
            sys.exit()
        guesses -= 1
        if guesses == 0:
            print("You are out of guesses")
            sys.exit()
    
    
    
