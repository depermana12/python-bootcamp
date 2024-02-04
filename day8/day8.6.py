import cipher


letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
          'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(cipher.logo)
restart = True


def caesar(message, key, option):
    cipher = ""
    for char in message:
        position = letter.index(char)
        if option == "decode":
            newposition = position - key
        elif option == "encode":
            newposition = position + key
        cipher += letter[newposition]
    print(f"The {option}d is: {cipher}")


while restart:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type shift number: \n"))
    caesar(text, shift, direction)
    tryagain = input("Do you want to restart? type 'yes' or 'no' ")
    if tryagain == "no":
        restart = False
