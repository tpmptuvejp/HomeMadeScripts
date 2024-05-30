#capital letters are not supported
def encode_w(word):
    encoded_word = ""
    for char in word:
        if char.isalpha():
            encoded_char = chr(ord(char) + 1)
            if encoded_char > 'z':
                encoded_char = 'a'
            encoded_word += encoded_char
        else:
            encoded_word += char
    return encoded_word

def decode_w(encoded_word):
    decoded_word = ""
    for char in encoded_word:
        if char.isalpha():
            decoded_char = chr(ord(char) - 1)
            if decoded_char < 'a':
                decoded_char = 'z'
            decoded_word += decoded_char
        else:
            decoded_word += char
    return decoded_word


def main():
    while True:
        print("(1) Encode")
        print("(2) Decode")
        print("(3) Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            word = input("Enter the word to encode: ")
            print("Encoded word:", encode_w(word))
        elif choice == "2":
            encoded_word = input("Enter the encoded word: ")
            print("Decoded word:", decode_w(encoded_word))
        elif choice == "3":
            print("Thanks for useing.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

#Developed in 2024 - SoloStudio
#SoloStudio
