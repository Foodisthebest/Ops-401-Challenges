# Ops Challenge 11

## Requirements

In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:

    Utilize the scapy library
    Define host IP
    Define port range or specific set of ports to scan
    Test each port in the specified range using a for loop
        If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
        If flag 0x14 received, notify user the port is closed.
        If no flag is received, notify the user the port is filtered and silently dropped

## Example

In this example, we're running against IP 192.168.1.1, starting at port 80 and ending at port 85.

```bash
sudo python3 opschallenge11.py 192.168.1.1 80 85
[sudo] password for woodstock: 

Port Scan of 192.168.1.1:
        Port 80 is Open
        Port 81 is Closed
        Port 82 is Closed
        Port 83 is Closed
        Port 84 is Closed
        Port 85 is Closed


```
