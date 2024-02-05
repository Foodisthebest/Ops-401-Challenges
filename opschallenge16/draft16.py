#!/usr/bin/env python

from sys import exit

from cli import parse_arguments

def scan(file_path):
    pass
    
def read_file(file_path):
    """
    Loads the key from the current directory named `key.key`
    """
    return open(file_path, "rb").read()

def scan_line(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.rstrip('\n')
    except FileNotFoundError:
        exit(f"The file '{file_path}' was not found.")
    except Exception as e:
        exit(f"An error occurred: {e}")

if __name__ == '__main__': 
    args = parse_arguments()

    file_location = args.FILE
    user_input = args.WORD

    for line in scan_line(args.FILE):
        print(line)

