#!/usr/bin/env python

from cli import parse_arguments


if __name__ == '__main__': 
    args = parse_arguments()

    if args.OFFENSIVE:
        print('offense')
    elif args.DEFENSIVE:
        print('defensive') 
