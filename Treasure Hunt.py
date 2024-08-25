# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:25:57 2024

@author: Lenovo
"""
import sys

print("""
           _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
//
""")

print("Welcome to the treasure hunt!!")
print("You are a pirate now.....")
print("HURRY the hunter is behind you")

choice1 = input('Do you want to go "left" or "right"? :').upper()
if choice1=="RIGHT":
    print("There was giant hole...........Game Over :(")
    sys.exit()
    
elif choice1=="LEFT":
    print("""Alright!
          now there is an unknown lake over here""")
    
    choice2=input('Do you want to "swim" or "wait" for the ship? :').upper()
    if choice2=="SWIM":
        print("Sorry Mr.Crocodile ate you...........Game over :(")
        sys.exit()
    elif choice2=="WAIT":
        print("""Yey!! 
              We have passed the lake""")
        choice3= input('Now do you want to open "Red","Yellow" or "Blue" door? : ').upper()
        if choice3=="RED" or choice3=="BLUE":
            print("Sorry you could'nt make....Game over  :(")
            sys.exit()
        elif choice3=="YELLOW":
            print("""Woohoo!!
                  You Win :)""")
        else:
            print("You have not enter a valid choice....Sorry only one chance GAME OVER")
    else:
        print("You have not enter a valid choice....Sorry only one chance GAME OVER")
 
else:
    print("You have not enter a valid choice....Sorry only one chance GAME OVER")           
   
            
            
            
            
            
            
            
            
            
            
            
            
            
            