#!/usr/bin/env python3

import os
from getpass import getpass
from sys import exit
from time import sleep



def print_file_to_screen(file_path, delay):
    """
    Offensive Mode
    """
    try:
        with open(file_path, 'r', encoding='latin-1') as word_list:
            for word in word_list:
                print(word.rstrip())
                sleep(delay)
    except Exception as e:
        exit(f"Issue: {e}")

def password_is_found(file_path, text):
    """
    Defensive Mode
    """
    try:
        with open(file_path, 'r', encoding='iso-8859-1') as word_list:
            if text in word_list.read():
                return True
            return False
    except Exception as e:
        exit(f"Issue: {e}")


menu = """\n\t\tSelect One of the following modes:

                     1. Offensive; Dictionary Iterator
                     2. Defensive; Password Recognized
                     3. Exit

                     > """

if __name__ == "__main__":

    while (user_input := input(menu)) != "3":
        file_path = input("\t\tEnter the filepath to the word list file: [rus.txt] ") or "rus.txt"
        if not os.path.exists(file_path):
            print("\n\t\tFile not found.")
        else:
            if user_input == "1":
                delay = int(input("\t\tEnter time delay between word checks (seconds): [1 second]"))
                print_file_to_screen(file_path, delay)
            elif user_input == "2":
                prompt = "\t\tEnter the password string: "
                password = getpass(prompt=prompt)
                if password_is_found(file_path, password):
                    print("\n\t\tPASSORD FOUND")
                    print("\t\tPassword was found in the word list. It's too common.\n")
                else:
                    print(f"\nPassword was not found in the word list.\n")
            else:
                print("\t\tThat's not an option.")
