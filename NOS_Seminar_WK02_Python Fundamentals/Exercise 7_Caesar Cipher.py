def caesar_cipher(message, key, mode):
    result = ""
    for char in message:
        if char.isalpha():
            shift = key if mode == "encrypt" else -key
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result


# Test encryption
print(caesar_cipher("HELLO", 3, "encrypt"))  # Output: KHOOR

# Test decryption
print(caesar_cipher("KHOOR", 3, "decrypt"))  # Output: HELLO
