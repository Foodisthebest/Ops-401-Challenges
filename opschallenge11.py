# Ops Challenge - Network Scanning with Scapy Part 1 of 3

# Script:                     Network Scanning with Scapy
# Author:                     Renona Gay
# Date of latest revision:    1/23/2024 
# Purpose:                    Ops 401 Challenge 11

#!/usr/bin/env python3


#! /usr/bin/env python

# These two lines imports the python system (python itself) so that you can 
# use it to make the code more adaptable, exit the program safely or handle errors "more gracefully"
# and makes the contents of sys readable on the screen.
import sys

# This line 
from scapy.all import Ether, IP, sniff, ARP, sr1, ICMP, TCP

p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
    p.show()









# Resources: https://g.co/bard/share/9950a8198b90
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-11/challenges/DEMO.md