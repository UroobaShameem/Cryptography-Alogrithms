morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def encode_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char != ' ':
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(' ')  # Use space to separate words
    return ' '.join(morse_code)

def decode_from_morse(morse_code):
    decoded_text = []
    morse_words = morse_code.split(' ')  # Split Morse code into words
    for morse_word in morse_words:
        if morse_word == '':
            decoded_text.append(' ')  # Preserve spaces between words
        else:
            # Invert the morse_code_dict to decode Morse code to characters
            for char, code in morse_code_dict.items():
                if code == morse_word:
                    decoded_text.append(char)
                    break
    return ''.join(decoded_text)

# Encryption:
text_to_encode = "Hello, World!"
print("Plain text: ", text_to_encode)
encoded_message = encode_to_morse(text_to_encode)
print("Encoded message:", encoded_message)

# Decryption:
morse_to_decode = "... ..- -. / ... . - / .. -. / .-- . ... - ,"
print("Cipher text: ", morse_to_decode)
decoded_message = decode_from_morse(morse_to_decode)
print("Decoded message:", decoded_message)
