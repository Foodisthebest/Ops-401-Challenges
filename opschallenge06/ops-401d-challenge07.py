#!/usr/bin/env python3

# argparse more "robust" because it creates flags and takes input from command line in a way that enforces rules on how input is taken in
# import argparse
# import sys

# URL: https://docs.python.org/3/library/argparse.html

import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('-k', type=pathlib.Path, help="Location of key file")
parser.add_argument('-m', type=str, help="Message")
parser.add_argument('-f', type=pathlib.Path, help="Location of file to Decrypt/Encrypt")
parser.add_argument('-e', action='store_true', help="Encrypt")
parser.add_argument('-d', action='store_true', help="Decrypt")


args = parser.parse_args()

# Check if both mutually exclusive flags are provided
if args.m and args.f:
    parser.error("Options -m and -m cannot be used at the same time.")

if args.e and args.d:
    parser.error("Options -e and -d cannot be used at the same time.")

print(args)

