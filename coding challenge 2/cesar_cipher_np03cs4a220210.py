import string
alphabets = (string.ascii_uppercase)


def wellcome():
    print('Welcome to the Caesar Cipher\nThis program encrypts and decrypts text using Caesar Cipher.')


def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.upper()
        if letter == " ":
            ciphertext += letter  # YO VANE KO WORDS PAXI KO SPACE HO
        if not letter == ' ':
            index = alphabets.find(letter)
            if index == -1:
                chiphertext += letter
            else:
                new_index = index + key
                if new_index >= 26:
                    new_index -= 26
                ciphertext += alphabets[new_index]
    print(ciphertext)  # output print garne ho
    againnn = input("Do you want to encrypt or decrypt again? (y/n)")
    if (againnn == "y"):
        combine()
    elif (againnn == "n"):
        thanks()


def decrypt(ciphertext, key):
    plaintext = ' '
    for letter in ciphertext:
        letter = letter.upper()
        if letter == " ":
            plaintext += letter  # YO VANE KO WORDS PAXI KO SPACE HO
        if not letter == ' ':
            index = alphabets.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += 26
                plaintext += alphabets[new_index]
    print(plaintext)  # output print ho
    againnn = input(
        "Would you like to encrypt or decrypt another message? (y/n):")
    if (againnn == "y"):
        combine()
    elif (againnn == "n"):
        thanks()


wellcome()


def enter_message():
    input_of_user = input('Would you like to encrypt(e) or decrypt(d)?: ')
    if 'd' or 'e':
        if input_of_user == 'e':
            text = input('What message would you like to encrypt: ')
            # Because the total alphabets number are 26
            Shift_number = int(input('what is the shift number:'))
            ciphertext = encrypt(text, Shift_number)

        elif input_of_user == 'd':
            text = input('What message would you like to decrypt: ')
            # Because the total alphabets number are 26
            Shift_number = int(input('what is the shift number:'))
            plaintext = decrypt(text, Shift_number)
    else:
        print("Invalid Mode")


def thanks():
    print("Thanks for using the program, goodbye!")


def combine():
    enter_message()


combine()
