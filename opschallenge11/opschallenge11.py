#! /usr/bin/env python3

# Ops Challenge - Network Scanning with Scapy Part 1 of 3

# Script:                     Network Scanning with Scapy
# Author:                     Renona Gay
# Date of latest revision:    1/23/2024 
# Purpose:                    Ops 401 Challenge 11


# These two lines import the python system (python itself) so that you can use it to make the code more adaptable, exit the program safely or handle errors "more gracefully"
# and makes the contents of sys readable on the screen.

import os
import sys

# This line imports the listed modules from the scapy library

from scapy.all import *

# Requirements

# In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:

#     Utilize the scapy library
#     Define host IP
#     Define port range or specific set of ports to scan
#     Test each port in the specified range using a for loop
#         If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
#         If flag 0x14 received, notify user the port is closed.
#         If no flag is received, notify the user the port is filtered and silently dropped


flags = sys.argv

host_ip = flags[1]
low_port = int(flags[2])
high_port = int(flags[3])

def check_port_open(target_ip, target_port):
    """
    Return 1 - Port Open
    Return 2 - Port Closed
    Return 3 - Port No Response
    """
    # Craft a TCP SYN packet
    syn_packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")

    # Send the packet and wait for a response
    response_packet = sr1(syn_packet, timeout=1, verbose=0)

    # Check if a response was received (does respond_packet = True ?)
    if response_packet:
        # Check if the response has the SYN-ACK flag set
        if response_packet.haslayer(TCP) and response_packet[TCP].flags == 0x12:
            # Craft a TCP RST packet to close the connection
            rst_packet = IP(dst=target_ip)/TCP(dport=target_port, sport=response_packet[TCP].dport, flags="R")
            send(rst_packet, verbose=0)
            return 1
        else:
            return 2
    else:
        return 3


if __name__ == "__main__":
    print(f"\nPort Scan of {host_ip}:")
    for port in range(low_port, high_port + 1):
        status = check_port_open(host_ip, port)
        if status == 1:
            print(f"\tPort {port} is Open")
        elif status == 2:
            print(f"\tPort {port} is Closed")
        elif status == 3:
            print(f"\tPort {port} is Filtered")
        else:
            print("Something wrong happened")
    print()


    










# Resources: https://g.co/bard/share/9950a8198b90
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-11/challenges/DEMO.md