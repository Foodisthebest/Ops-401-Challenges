#!/usr/bin/env python3


import os

from cryptography.fernet import Fernet

from cli import parse_arguments


def generate_key(path):
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open(path, "wb") as key_file:
        key_file.write(key)


def read_key(path):
    """
    Loads the key from path
    """
    return open(path, "rb").read()


def encrypt_file(file_name, key):
    """
    Delete the existing target file and replace it entirely with the encrypted version.
    """
    message = read_file(file_name)
    if delete_file(file_name):
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
    key_contents = read_file(key)
    f = Fernet(key_contents)
    m = message.encode()
    return f.encrypt(m)


def decrypt_message(encrypted, key):
    """
    Decrypts message.
    """
    key_contents = read_file(key)
    f = Fernet(key_contents)
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
    
def encrypt_folder(folder_path, key):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            encrypt_file(file_path, key)

# Recursively decrypt a single folder that was encrypted by this tool
def decrypt_folder(folder_path, key):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            decrypt_file(file_path, key)


if __name__ == "__main__":
    args = parse_arguments()
    key_path = args.key

    if not os.path.exists(args.key):
        generate_key(args.key)

    if args.file:
        if not os.path.exists(args.file):
            exit("File not found.")
    elif args.FOLDER:
        if not os.path.exists(args.FOLDER):
            exit(f"{folder_path} not found.")

    # Read the key from the key file
    key = read_key(args.key)
    if args.ENCRYPT:
        if args.file:
            file_path = args.file
            encrypt_file(file_path, key_path)
            print(f"File {file_path} encrypted successfully.")
            exit()
            # TODO: There's no error check here.
        elif args.message:
            message = " ".join(args.message)
            byte_string = encrypt_message(message, str(key_path))
            output = byte_string.decode("utf-8")
            print(f"{output}")
            exit()
        elif args.FOLDER:
            folder_path = args.FOLDER
            encrypt_folder(folder_path, key_path)
            print(f"Folder {folder_path} encrypted successfully.")
            exit()

    elif args.DECRYPT:
        if args.file:
            file_path = args.file
            decrypt_file(file_path, key_path)
            print(f"File {file_path} decrypted successfully.")
            exit()

        elif args.message:
            message = " ".join(args.message)
            byte_string = decrypt_message(message, str(key_path))
            output = byte_string.decode("utf-8")
            print(f"{output}")
            exit()

        elif args.FOLDER:
            folder_path = args.FOLDER
            decrypt_folder(folder_path, key_path)
            print(f"Folder {folder_path} decrypted successfully.")
            exit()
