#CAESAR CIPHER
#Print ASCII art
from art import logo
print(logo)

#Define variable(s)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Define caesar cipher function
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet: #number/symbol/space
            end_text += char
        elif char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")

#Run the program...
restart = True
while restart == True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #For shift entries greater than the number of letters in the alphabet...
    if shift > 26:
        shift = shift % 26 #shift by remainder
    
    #Call the caesar cipher function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    #Restart?
    go_again = input("\nType 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
    if go_again == "no":
        restart = False
        print("Goodbye.")

