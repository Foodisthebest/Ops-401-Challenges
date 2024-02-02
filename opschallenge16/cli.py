import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="challenge16",
        description="Automated Brute Force Wordlist Attack Tool Part 1 of 3",
        epilog="Thanks for using %(prog)s! :)",
    )
    parser.add_argument(
        "-O", 
        "--OFFENSIVE",
        action="store_true", help="Mode 1: Offensive; Dictionary Iterator"
    )
    parser.add_argument(
        "-D",
        "--DEFENSIVE",
        action="store_true", help="Mode 2: Defensive; Password Recognized"
    )

    

    return parser.parse_args()
