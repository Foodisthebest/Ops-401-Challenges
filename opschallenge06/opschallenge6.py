#!/usr/bin/env python3

import os 

from cryptography.fernet import Fernet
# https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def read_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def encrypt_file(file_name, key):
    message = open(file_name, "r").read()
    return encrypt_message(message, key)


def decrypt_file(encrypted_file, key):
    message = open(file_name, "r").read()
    return 

def encrypt_message(message, key):
    f = Fernet(key)
    m = message.encode()
    return f.encrypt(m)

def decrypt_message(encrypted, key):
    f = Fernet(key)
    return f.decrypt(encrypted)


if __name__ == '__main__':

    file = "sample.txt"
    # generate and write a new key
    generate_key()
    key = read_key()
    message = "some secret message"
    encrypted = encrypt_message(message, key)
    decrypted_encrypted = decrypt_message(encrypted, key)
    encrypted_file = encrypt_file(file, key)

    print(f"""
        Original Message: {message}
        Encrypted Text: {encrypted}
        Decrypted Text: {decrypted_encrypted}
        
        Encrypted File: {encrypted_file}
        """)