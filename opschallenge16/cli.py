import argparse
import pathlib

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="challenge16",
        description="Automated Brute Force Wordlist Attack Tool Part 1 of 3",
        epilog="Thanks for using %(prog)s! :)",
    )
    parser.add_argument(
        "-O",
        "--OFFENSIVE",
        action="store_true",
        required=False,
        help="Offensive; Dictionary Iterator",
    )
    parser.add_argument(
        "-D",
        "--DEFENSIVE",
        action="store_true",
        required=False,
        help="Defensive; Password Recognized",
    )
    parser.add_argument(
        "-F",
        "--FILE",
        type=lambda p: pathlib.Path(p).absolute(),
        required=True,
        help="Location of word list",
    )
    parser.add_argument(
        "-W", 
        "--WORD",
        nargs="*", type=str, help="Message"
    )
    return parser.parse_args()