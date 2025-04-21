from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
cipher = Fernet(KEY)


def encrypt_message(message):
    return cipher.encrypt(message.encode())


def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message).decode()
