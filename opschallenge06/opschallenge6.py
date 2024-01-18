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

def encrypt_file():
    pass

def decrypt_file():
    pass

def encrypt_message():
    pass
    
def decrypt_message():
    pass

if __name__ == '__main__':

    # generate and write a new key
    generate_key()
    key = read_key()
    message = "some secret message".encode()
    # initialize the Fernet class
    f = Fernet(key)
    encrypted = f.encrypt(message)
    decrypted_encrypted = f.decrypt(encrypted)
    print(f"""
        Original Message: {message}
        Encrypted Text: {encrypted}
        Decrypted Text: {decrypted_encrypted}
        """)