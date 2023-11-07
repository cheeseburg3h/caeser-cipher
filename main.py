from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_ammount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_ammount) % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text

def decrypt(plain_text, shift_ammount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_ammount) % len(alphabet)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'quit' to quit the program:\n")
    if direction == 'quit':
            print("Goodbye!")
            break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    match direction:
        case 'encode':
            encrypted_message = encrypt(text, shift)
            print(f"The encoded text is: {encrypted_message}")

        case 'decode':
            decrypted_message = decrypt(text, shift)
            print(f"The decoded text is: {decrypted_message}")

        case _:
            print("Invalid input, please try again!")
   
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == 'no':
        print("Goodbye!")
        break


