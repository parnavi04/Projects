# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:03:48 2024

@author: Lenovo
"""

#Coffee Machine Code
#Expresso: water: 50ml, Coffee: 18gm
#Lattee: Water:200ml, coffee: 24gm, milk: 150ml
#Cappuccino: Water: 250ml, Coffee:24gm, Milk:100ml
#Stock: Water: 300ml, Coffee: 100gm, Milk:200ml
import sys
stock_water = 300
stock_coffee = 100
stock_milk = 200

expresso_cost= 1.5
lattee_cost = 2.5
cappuccino_cost = 3

i =True
while i:

    choice = input("What would you like to order?(expresso:e,Lattee:l,Cappuccino:c, Exit:0): ")

    if choice=="e":
        quaters =int(input("How many quaters? ")) #0.25$
        dime =int(input("How many dime? "))  #0.10$
        penny =int(input("How many penny? "))  #0.01$
        nickel =int(input("How many nickel? ")) #0.05$
        
        total_money = (quaters*0.25)+(dime* 0.10)+(penny*0.01)+(nickel*0.05)
        if total_money<expresso_cost:
            print("please insert more money for your order")
            
        if total_money>expresso_cost:
            money_return = total_money - expresso_cost
            
            if stock_water>50 and stock_coffee>18:
                stock_water -=50
                stock_coffee -=18
                print("Your change is",round(money_return,2),"$")
                print("Enjoy your coffee ")
            else:
                print("Sorry, we are out of stock!")
    
    if choice =="l":
        quaters =int(input("How many quaters? ")) #0.25$
        dime =int(input("How many dime? "))  #0.10$
        penny =int(input("How many penny? "))  #0.01$
        nickel =int(input("How many nickel? ")) #0.05$
    
        total_money = (quaters*0.25)+(dime* 0.10)+(penny*0.01)+(nickel*0.05)
        if total_money<lattee_cost:
            print("please insert more money for your order")
        elif total_money>lattee_cost:
            money_return = total_money - lattee_cost
            
            if stock_water>200 and stock_coffee>24 and stock_milk>150:
                stock_water-=200
                stock_coffee-=24
                stock_milk-=150
                print("Your change is",round(money_return,2),"$")
                print("Enjoy your coffee ")
            else:
                print("Sorry, we are out of stock!")
    
    if choice =="c":
        quaters =int(input("How many quaters? ")) #0.25$
        dime =int(input("How many dime? "))  #0.10$
        penny =int(input("How many penny? "))  #0.01$
        nickel =int(input("How many nickel? ")) #0.05$
        
        total_money = (quaters*0.25)+(dime* 0.10)+(penny*0.01)+(nickel*0.05)
        if total_money<cappuccino_cost:
            print("please insert more money for your order")
        elif total_money>cappuccino_cost:
            money_return = total_money - cappuccino_cost
            
            if stock_water>250 and stock_coffee>24 and stock_milk>200:
                stock_water-=250
                stock_coffee-=24
                stock_milk-=200
                print("Your change is",round(money_return,2),"$")
                print("Enjoy your coffee ")
            else:
                print("Sorry, we are out of stock!")
                
    if choice=="report":
        print("Water= ",stock_water)
        print("Coffee= ",stock_coffee)
        print("Milk= ",stock_milk)
        
    if choice =="0":
        sys.exit()
        
    
    
    
    