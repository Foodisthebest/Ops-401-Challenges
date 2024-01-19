#!/usr/bin/env python3

import os

from cryptography.fernet import Fernet

# https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# worked with TA Aaron Imbrock


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
    """
    Delete the existing target file and replace it entirely with the encrypted version.
    """
    message = read_file(file_name)
    print(f"encrypt message is {message}")
    if delete_file(file_name):
        print("File exists")
        message = encrypt_message(message, key)
        write_to_file(message, file_name)
        return True
    else:
        print("encrypt_file() failed.")
        return False


def decrypt_file(file_name, key):
    """
    Delete the encrypted target file and replace it entirely with the decrypted version.
    """
    message = read_file(file_name)
    print(f"decrypt message is {message}")
    if delete_file(file_name):
        message = decrypt_message(message, key)
        write_to_file(message, file_name)
        return True
    else:
        print("decrypt_file failed")
        return False


def encrypt_message(message, key):
    """
    Encrypts message.
    """
    f = Fernet(key)
    m = message.encode()
    return f.encrypt(m)


def decrypt_message(encrypted, key):
    """
    Decrypts message.
    """
    f = Fernet(key)
    return f.decrypt(encrypted)


def read_file(file_name):
    """
    Loads file and returns contents
    """
    with open(file_name, "r") as file:
        message = file.read()
    return message


def write_to_file(message, file_name):
    """
    Writes the message to the specified file.
    Returns True on success, False on failure.
    """
    try:
        with open(file_name, "wb") as file:
            file.write(message)
        return True
    except Exception as e:
        print(e)
        return False


def delete_file(file_name):
    """
    Delete file
    Returns True
    Returns False
    """
    try:
        os.remove(file_name)
        return True
    except Exception as e:
        print(e)
        return False

mode = """Select One of the following options:
                     1. Encrypt a file
                     2. Decrypt a file
                     3. Encrypt a message
                     4. Decrypt a message
                     5. Exit
                     > """

if __name__ == "__main__":
    key_path = "key.key"
    
    # Check if the key file exists
    if not os.path.exists(key_path):
        generate_key()

    # Read the key from the key file
    key = read_key()

    while (user_input := input(mode)) != "5"
        print(f"user_input is {user_input} and {type(user_input)}")
        if user_input == "1" or user_input == "2":
            file_path = input("Enter the filepath to the target file: ")
            if not os.path.exists(file_path):
                print("File not found.")
                exit()
        elif user_input == "3" or user_input == "4":
            message = input("Enter the cleartext string: ")

        if user_input == "1":
            encrypt_file(file_path, key)
            print(f"{file_path} encrypted successfully.")
        elif user_input == "2":
            decrypt_file(file_path, key)
            print(f"{file_path} decrypted successfully.")
        elif user_input == "3":
            print(encrypt_message(message, key))
        elif user_input == "4":
            print(decrypt_message(message, key))
        else:
            print("That is not an option.")
