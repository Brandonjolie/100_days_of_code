from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(text, shift, direction):
    newtext = ""
    while shift > 26:
        shift = shift % 26
    for item in text:
        if item in alphabet:
            curent_index = alphabet.index(item)
            if direction == 'encode':
                word = 'encoded'
                new_index = curent_index+shift
            elif direction == 'decode':
                word = 'decoded'
                new_index = curent_index-shift
            if new_index > len(alphabet)-1:
                new_index -= (len(alphabet))
            newtext += alphabet[new_index]
        else:
            newtext += item
    print(f"The {word} text is {newtext}")


print(logo)
running = True
while running == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(text, shift, direction)
    val = input('Do you want to restart the program? ').lower()
    if val == 'yes':
        pass
    else:
        running = False
