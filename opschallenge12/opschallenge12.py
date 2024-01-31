#! /usr/bin/env python3

# Ops Challenge - Network Scanning with Scapy Part 2 of 3

# Script:                     Network Scanning with Scapy
# Author:                     Renona Gay
# Date of latest revision:    1/30/2024 
# Purpose:                    Ops 401 Challenge 12


import ipaddress
import os
import sys

# This line imports the listed modules from the scapy library

from scapy.all import *

from cli import parse_arguments

flags = sys.argv



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
    # print(response_packet.show())
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


mode = """Select One of the following options:
                     1. TCP Port Range Scanner mode
                     2. ICMP Ping Sweep mode
                     3. Exit
                     > """


if __name__ == "__main__":

    args = parse_arguments()

    if args.TCP:

        print("TCP Port Range Scanner mode")
        print(f"\nPort Scan of {args.ip_address}:")
        for port in range(args.start_port, args.end_port + 1):
            status = check_port_open(args.ip_address, port)
            if status == 1:
                print(f"\tPort {port} is Open")
            elif status == 2:
                print(f"\tPort {port} is Closed")
            elif status == 3:
                print(f"\tPort {port} is Filtered")
            else:
                print("Something wrong happened")
        print()
    elif args.ICMP:
        
        print("ICMP Ping Sweep mode")



    










# Resources: https://g.co/bard/share/9950a8198b90
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-11/challenges/DEMO.md