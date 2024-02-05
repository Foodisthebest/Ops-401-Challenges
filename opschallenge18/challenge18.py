#!/usr/bin/env python3

from sys import exit
from zipfile import ZipFile


def read_file_to_list(file_path):
    """
    Read the entire contents of a file and return a list of words.
    """
    try:
        with open(file_path, 'r', encoding='latin-1') as word_list:
            return [word.rstrip() for word in word_list]
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Issue: {e}")
        return []

def unzip(file_path, password):
    # Add the ZIP file brute force functionality
    try:
        with ZipFile(file_path, 'r') as file:
            file.extractall(pwd=bytes(password, 'utf-8'))
        return True
    except Exception:
        return False
                

if __name__ == "__main__":

    pw_file_path = input("Password file location: [rus.txt]: ") or "rus.txt"
    zip_file_path = input("Zip file location: [zipencrypted.zip]: ") or "zipencrypted.zip"

    password_list = read_file_to_list(pw_file_path)

    for word in password_list:
        if unzip(zip_file_path, word):
            print(f"\nSuccess. {word} is the password for {zip_file_path} \n")
            exit(0)
    print(f"\nNo words in {pw_file_path} decrypted {zip_file_path}\n ")
    exit(0)
        



