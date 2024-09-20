myDict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def to_morse_code(message):
    morse_code = ''
    for char in message.upper():
        if char in myDict:
            morse_code += myDict[char] + ' '
    return morse_code

def main():
    while True:
        choice = input(
            "Choose an option:\npress 1 to convert text to Morse Code\npress 2 to quit\n")
        if choice == '1':
            message = input("Enter a message to convert to Morse Code: ")
            morse_code = to_morse_code(message)
            print(morse_code)

        elif choice == '2':
            print("Task exited successfully.")
            break

        else:
            print("Invalid choice, please choose from the available options.")

if __name__ == "__main__":
    main()