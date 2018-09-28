import sys
from cs50 import get_string

def main():

    #If args are good: let's go
    if len(sys.argv) == 2:

        key = int(sys.argv[1])
        plain = get_string("plaintext: ")
        usefulKey = key
        cipher = ''

        #encode each character in the plaintext
        for symbol in plain:

            if symbol.isalpha():
                numb = ord(symbol)
                numb += usefulKey

                if symbol.isupper():
                    while numb < ord('A'):
                        numb += 26
                    while numb > ord('Z'):
                        numb -= 26

                elif symbol.islower():
                    while numb < ord('a'):
                        numb += 26
                    while numb > ord('z'):
                        numb -= 26

                cipher += chr(numb)

            else:
                cipher += symbol

        print(f"ciphertext: {cipher}")

    #If args are bad: error
    else:
        return -1


if __name__ == "__main__":
    main()