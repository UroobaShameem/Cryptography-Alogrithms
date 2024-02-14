def main():
    print("Vigenere Cipher _ Method1")

    # Define the Vigenere table
    vigenere_table = [[(chr((i + j) % 26 + ord('A'))) for j in range(26)] for i in range(26)]

    # Define the key
    key = "LOCK"

    # Print the Vigenere table with headings
    print("Vigenere Cipher Table:")
    print("    ", end="")
    for i in range(26):
        print(f"{chr(ord('A') + i):<3}", end="")
    print()
    for i in range(26):
        print(f"{chr(ord('A') + i):<4}", end="")
        for j in range(26):
            print(f"{vigenere_table[i][j]:<3}", end="")
        print()
    print()

    # Get the plaintext from the user
    plaintext = input("Enter the plaintext: ").upper()

    # Encrypt the plaintext using the Vigenere Cipher
    encrypted_text = ""
    j = 0
    for i in range(len(plaintext)):
        c = plaintext[i]
        if c.isalpha():
            row = ord(key[j % len(key)]) - ord('A')
            col = ord(c) - ord('A')
            encrypted_text += vigenere_table[row][col]
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
            row = ord(key[j % len(key)]) - ord('A')
            col = vigenere_table[row].index(c)
            decrypted_text += chr(col + ord('A'))
            j += 1
        else:
            decrypted_text += c

    # Display the decrypted text
    print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()
