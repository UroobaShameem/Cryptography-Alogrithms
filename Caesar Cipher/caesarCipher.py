def caesar_encrypt(text, shift):
    result = []

    for char in text:
        if char.isalpha():
            base_char = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base_char + shift) % 26 + base_char))
        else:
            result.append(char)  

    return ''.join(result)


def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def main():
    plaintext = input("Enter the text to encrypt:\n")

    try:
        shift_value = int(input("Enter the shift value (an integer):\n"))
        ciphered_text = caesar_encrypt(plaintext, shift_value)
        deciphered_text = caesar_decrypt(ciphered_text, shift_value)

        print(f"Original text: {plaintext}")
        print(f"Ciphered text: {ciphered_text}")
        print(f"Deciphered text: {deciphered_text}")
    except ValueError:
        print("Invalid shift value. Please enter a valid integer.")


if __name__ == "__main__":
    main()
