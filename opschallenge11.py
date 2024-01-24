# Ops Challenge - Network Scanning with Scapy Part 1 of 3

# Script:                     Network Scanning with Scapy
# Author:                     Renona Gay
# Date of latest revision:   1/23/2024 
# Purpose:                    Ops 401 Challenge 11

#!/usr/bin/env python3


#! /usr/bin/env python

import sys
from scapy.all import sr1,IP,ICMP

p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
    p.show()

