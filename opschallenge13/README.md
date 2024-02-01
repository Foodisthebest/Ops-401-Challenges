# Ops Challenge 13

## Objectives

The final iteration of your network scanning tool will perform the following:

    Ping an IP address determined by the user.
    If the host exists, scan its ports and determine if any are open.

## Tasks

Here's a general outline of how to achieve the desired outcome.

    In Python, combine the two modes (port and ping) of your network scanner script.
    Eliminate the choice of mode selection.
    Continue to prompt the user for an IP address to target.
    Move port scan to its own function.
    Call the port scan function if the host is responsive to ICMP echo requests.
    Print the output to the screen.

## How To Use

`-i` for the IP Address.
`-s` is the starting Port.
`-e` is the ending Port.

```bash
$ sudo ./opschallenge13.py -i 4.2.2.2 -s 80 -e 85
Port Scan Mode
4.2.2.2 is Up.

Port Scan of 4.2.2.2:
        Port 80 is Filtered
        Port 81 is Filtered
        Port 82 is Filtered
        Port 83 is Filtered
        Port 84 is Filtered
        Port 85 is Filtered

```