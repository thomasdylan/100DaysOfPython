import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    cipher_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == 'encode':
            new_position = position + shift_amount
        else:
            new_position = position - shift_amount
        cipher_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {cipher_text}")


print(art.logo)

game_active = True

while game_active == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    continue_game = input(
        '\n\nDo you want to encode or decode another message? "yes" to continue, any other input to quit: ').lower()
    if continue_game != 'yes':
        game_active == False
        print("Goodbye")
