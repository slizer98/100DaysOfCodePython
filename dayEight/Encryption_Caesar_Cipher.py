alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art_Caesar import logo
print(logo)

def caesar(text, shift, cipher_direction):
    answer = ''
    for letter in text:

        if letter not in alphabet:
            answer += letter
            continue

        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift
            if new_position > len(alphabet) - 1:
                new_position = new_position - len(alphabet)
        
        elif cipher_direction == "decode":
            new_position = position - shift
        answer += alphabet[new_position]

    print(f"The {cipher_direction}d text is {answer}")

new_game = "yes"
while new_game != "no":    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > len(alphabet):
        shift = shift % len(alphabet)
        
    caesar(text=text, shift=shift, cipher_direction=direction)

    new_game = input("Do you want to play again? Type 'yes' or 'no'.\n").lower()

print("Goodbye 👋")