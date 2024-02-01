from os import system, name, environ, geteuid
from sys import exit


def clear_screen():
    if name == "nt":
        _ = system("cls")
    _ = system("clear")

def check_privileges(message="You need to run this script with sudo or as root."):
    if not environ.get("SUDO_UID") and geteuid() != 0:
        # raise PermissionError(message)
        exit(message)
        