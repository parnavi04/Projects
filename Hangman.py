#Hangman

import random
import sys

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''',  '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',  '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']    
        
       
#for a list of hidden words
words = ["Archaeology", "Chrysanthemum", "Hippocampus", "Kaleidoscopic", "Mitochondria", "Phylogeny",
"Quizzical","Rhododendron","Sesquipedalian","Synchronization","Aardvark","Chameleon","Crocodile","Hippopotamus","Kaleidoscope","Knitting","Laboratory","Microphone","Pterodactyl","Submarine","Bicycle","Dolphin","Elephant","Giraffe","Helicopter","Kangaroo",
"Penguin","Pyramid", "Rainbow", "Volcano"]


#first part
print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)
                

w = random.randint(0, len(words)-1)
hidden_word = words[w].lower()
print("\n")
print("Hidden word: ")
print("_ "*len(hidden_word))

blank = "_ "*len(hidden_word)
blanks = blank.split()
lives = 0
#print(hidden_word)
while True:

    guess = input("\nGuess a letter: ").lower()
    guess_list = []
    chance =0
    repeat_guess = guess_list.count(guess)
    

    
    for l in range(len(hidden_word)):
        
        if guess == hidden_word[l]:
            blanks[l] = hidden_word[l]
            guess_list.append(guess)
    if  repeat_guess > 1:
        print(f"You have already guessed {guess}")        
    
    if guess not in hidden_word:
        print(f"Your guess {guess} is not right, You lost one live")
        print(stages[lives])
        lives +=1
        if lives ==7:
            print("You Lose")
            print(hidden_word)
            sys.exit()
        
    print(*blanks)
    if "_" not in blanks:
        print("You Win!")
        sys.exit()










