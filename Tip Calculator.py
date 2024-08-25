#Tip Calculator
print("Welcome to the tip calculator :)")

bill = float(input("What is your bill? "))

percent = int(input("How much tip would you like to give (10, 12, 15): "))

people = int(input("How many people are going to split the bill: "))

total_bill = bill +bill * (percent/100)
each_bill = total_bill/people

print(f"Each person should pay: ${round(each_bill,2)}")
