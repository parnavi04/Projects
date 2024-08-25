# password generator
import random
print("Welcome to PyPassword generator!")

total_letters = int(input("How many letters do you want in your password: \n"))
total_numbers = int(input("How many numbers do you want in your password: \n"))
total_symbols = int(input("How many symbols do you want in your password: \n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

final_list = []
for i in range(total_letters):
    random_index_letter = random.randint(0,len(letters)-1)
    final_list.append(letters[random_index_letter])
    
for j in range(total_numbers):
    random_index_number = random.randint(0,len(numbers)-1)
    final_list.append(numbers[random_index_number])
    
for k in range(total_symbols):
    random_index_symbol = random.randint(0,len(symbols)-1)
    final_list.append(symbols[random_index_symbol])
    



print("Your new password is: ")
for n in range(len(final_list)):
    random_index = random.randint(0,len(final_list)-1)
    print(final_list[random_index],end="")
    
print("\nTHANK YOU FOR VISITING PYPASSWORD")