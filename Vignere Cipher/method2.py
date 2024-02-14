def main():
    print("Vigenere Cipher _ Method2")

    # Define the key
    key = "PASCAL"

    # Get the plaintext from the user
    plaintext = input("Enter the plaintext: ").upper()

    # Encrypt the plaintext using the Vigenere Cipher method 2
    encrypted_text = ""
    j = 0
    for i in range(len(plaintext)):
        c = plaintext[i]
        if c.isalpha():
            key_char = key[j % len(key)]
            shift = ord(key_char) - ord('A')
            encrypted_char = chr((ord(c) + shift - ord('A')) % 26 + ord('A'))
            encrypted_text += encrypted_char
            j += 1
        else:
            encrypted_text += c

    # Display the encrypted text
    print("Encrypted text:", encrypted_text)

    # Decrypt the encrypted text
    decrypted_text = ""
    j = 0
    for i in range(len(encrypted_text)):
        c = encrypted_text[i]
        if c.isalpha():
            key_char = key[j % len(key)]
            shift = ord(key_char) - ord('A')
            decrypted_char = chr((ord(c) - shift - ord('A') + 26) % 26 + ord('A'))
            decrypted_text += decrypted_char
            j += 1
        else:
            decrypted_text += c

    # Display the decrypted text
    print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()
