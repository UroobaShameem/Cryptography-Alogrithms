def streamcipher(input_data, key):
    if isinstance(input_data, str):  # Check if input_data is a string (plaintext)
        plaintext = int(input_data, 2)
        key = int(key, 2)
        ciphertext = plaintext ^ key
        return bin(ciphertext)[2:]  # Return ciphertext as binary string

    elif isinstance(input_data, int):  # Check if input_data is an integer (ciphertext)
        ciphertext = input_data
        key = int(key, 2)
        plaintext = ciphertext ^ key
        return bin(plaintext)[2:]  # Return plaintext as binary string

    else:
        raise ValueError("Invalid input type. Please provide either a binary string or an integer.")

# Example usage for encryption:
plaintext_binary = "101010"
key_binary = "110011"
encrypted_binary = streamcipher(plaintext_binary, key_binary)
print("Ciphertext:", encrypted_binary)

# Example usage for decryption:
ciphertext_binary = int(encrypted_binary, 2)
decrypted_binary = streamcipher(ciphertext_binary, key_binary)
print("Decrypted plaintext:", decrypted_binary)
