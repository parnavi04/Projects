#Ceaser Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

next_choice = True

 #defining functions
def encode(text, shift_key):
    encrypted = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_key
            new_letter = alphabet[new_position % 26]
            encrypted += new_letter
        else:
            encrypted += letter
    print(f"The encode message is: {encrypted}")
    
def decode(text, shift_key):
    decrypted =""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_key
            new_letter = alphabet[new_position  % 26]
            decrypted += new_letter
        else:
            decrypted += letter
    print(f"The decoded message is: {decrypted}")
        
        
def Ceaser(direction, text, shift_key):
    if direction.lower() == "encode":
        encode(text, shift_key)
           
    elif direction.lower()== "decode":
        decode(text, shift_key)
        
    else :
        print("Invalid choice")


while next_choice:
    print('''          88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                              ''')
    #take all the input
    direction = input('Do you want to "encode" or "decode": \n')
    text = input("Enter the message: \n").lower()
    shift_key = int(input("Enter the shift key: \n"))
    
    Ceaser(direction, text, shift_key)
    choice = input('Type "yes" if youn want to do it again. Otherwise type "no" ').lower()
    if choice == "yes":
        next_choice = True
    elif choice == 'no':
        next_choice = False        
    else:
        print("Choice not found")
        
       

















