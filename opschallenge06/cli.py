import argparse
import pathlib

# URL: https://docs.python.org/3/library/argparse.html
# https://docs.python.org/3/howto/argparse.html


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="opschallenge7",
        description="Helpful file encryption tool.",
        epilog="Thanks for using %(prog)s! :)",
    )
    encryption_group = parser.add_mutually_exclusive_group(required=True)
    encryption_group.add_argument(
        "-E", "--ENCRYPT", action="store_true", help="Encrypt"
    )
    encryption_group.add_argument(
        "-D", "--DECRYPT", action="store_true", help="Decrypt"
    )
    parser.add_argument(
        "-k",
        "--key",
        type=lambda p: pathlib.Path(p).absolute(),
        required=True,
        help="Location of key file",
    )
    exclusion_group = parser.add_mutually_exclusive_group()
    exclusion_group.add_argument("-m", "--message", nargs="*", type=str, help="Message")
    exclusion_group.add_argument(
        "-f",
        "--file",
        type=lambda p: pathlib.Path(p).absolute(),
        help="Location of file to Decrypt/Encrypt",
    )
    exclusion_group.add_argument(
        "-F",
        "--FOLDER",
        type=lambda p: pathlib.Path(p).absolute(),
        help="Location of folder to Decrypt/Encrypt",
    )

    return parser.parse_args()
