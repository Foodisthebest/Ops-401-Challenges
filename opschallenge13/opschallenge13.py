#! /usr/bin/env python3

# Ops Challenge - Network Scanning with Scapy Part 3 of 3

# Script:                     Network Scanning with Scapy
# Author:                     Renona Gay, worked with TA Aaron Imbrock
# Date of latest revision:    1/31/2024 
# Purpose:                    Ops 401 Challenge 13

from utils import clear_screen, check_privileges

check_privileges()
# clear_screen()

import ipaddress
import sys

from scapy.all import send, srp, sr1, srp1, ARP, Ether, ICMP, IP, TCP

from cli import parse_arguments

def get_mac(ip_address):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_address)
    result, _ = srp(arp_request, timeout=2, verbose=False)
    if result:
        return result[0][1].hwsrc
    else:
        return None

def portscan(target_ip, target_port):
    """
    Return 1 - Port is Open
    Return 2 - Port is Closed
    Return 3 - Port is No Response
    """
    # Craft a TCP SYN packet
    syn_packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")

    # Send the packet and wait for a response
    response = sr1(syn_packet, timeout=1, verbose=0)
    # print(response_packet.show())
    # Check if a response was received (does respond_packet = True ?)
    if response:
        # Check if the response has the SYN-ACK flag set
        if response.haslayer(TCP) and response[TCP].flags == 0x12:
            # Craft a TCP RST packet to close the connection
            rst_packet = IP(dst=target_ip)/TCP(dport=target_port, sport=response[TCP].dport, flags="R")
            send(rst_packet, verbose=0)
            return 1
        else:
            return 2
    else:
        return 3
    
def icmp_ping(ip_address):
    """
    Return Codes
    1 - Host is not responding
    0 - Host is responding
    3 - Host is filtering ICMP traffic
    4 - Unknown Issue
    """
    icmp_request = IP(dst=str(ip_address))/ICMP()
    response = sr1(
        icmp_request,
        timeout=2,
        verbose=False
    )

    if response is None:
        return 1
    elif response.type == 0:
        return 0
    elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
        return 3
    else:
        return 4

if __name__ == "__main__":

    args = parse_arguments()

    # TODO
    # We do no type checking of any user inputs:
    # [] - Is --ping_range a valid ip network?
    # Ctrl-C doesn't work. You have to close the terminal.
    # https://stackoverflow.com/questions/35974341/scapy-sending-packets-until-ctrlc-not-working

    if args.ip_address:
        address = args.ip_address
        if icmp_ping(address) == 0:
            print(f"Port Scan Mode")
            print(f"{address} is Up.")
            print(f"\nPort Scan of {args.ip_address}:")
            for port in range(args.start_port, args.end_port + 1):
                status = portscan(args.ip_address, port)
                if status == 1:
                    print(f"\tPort {port} is Open")
                elif status == 2:
                    print(f"\tPort {port} is Closed")
                elif status == 3:
                    print(f"\tPort {port} is Filtered")
                else:
                    print("Something went wrong")

  