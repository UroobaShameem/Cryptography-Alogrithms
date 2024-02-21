def vernam_encrypt(plaintext, key):
    # Ensure the key is at least as long as the plaintext
    if len(key) < len(plaintext):
        raise ValueError("Key length must be at least as long as plaintext")

    # Convert plaintext and key to uppercase
    plaintext = plaintext.upper()
    key = key.upper()

    # Perform XOR operation for each character
    encrypted_text = ""
    for i in range(len(plaintext)):
        encrypted_char = chr(((ord(plaintext[i]) - 65) + (ord(key[i]) - 65)) % 26 + 65)
        encrypted_text += encrypted_char

    return encrypted_text

def vernam_decrypt(encrypted_text, key):
    # Ensure the key is at least as long as the encrypted text
    if len(key) < len(encrypted_text):
        raise ValueError("Key length must be at least as long as encrypted text")

    # Convert key to uppercase
    key = key.upper()

    # Perform XOR operation for each character
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        decrypted_char = chr(((ord(encrypted_text[i]) - ord(key[i])) % 26) + 65)
        decrypted_text += decrypted_char

    return decrypted_text

# Take input from the user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

# Encrypt the message
encrypted_text = vernam_encrypt(plaintext, key)
print("Encrypted Text:", encrypted_text)

# Decrypt the message
decrypted_text = vernam_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
