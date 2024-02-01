# Ops Challenge 12

Add the following features to your Network Security Tool:

    User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday's feature set
    ICMP Ping Sweep tool
        Prompt user for network address including CIDR block, for example `10.10.0.0/24`

            Careful not to populate the host bits!

        Create a list of all addresses in the given network
        Ping all addresses on the given network except for network address and broadcast address
            If no response, inform the user that the host is down or unresponsive.
            If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
            Otherwise, inform the user that the host is responding.
        Count how many hosts are online and inform the user.

## How to Use:

`$ sudo ./opschallenge12.py -I -C $IPCIDR Block`

Example:

```bash
$ sudo ./opschallenge12.py -I -C 4.2.2.0/28
ICMP Ping Sweep mode
Checking IP 4.2.2.1: Responding. Host is up.
Checking IP 4.2.2.2: Responding. Host is up.
Checking IP 4.2.2.3: Responding. Host is up.
Checking IP 4.2.2.4: Responding. Host is up.
Checking IP 4.2.2.5: Responding. Host is up.
Checking IP 4.2.2.6: Responding. Host is up.
Checking IP 4.2.2.7: Not Responding.
Checking IP 4.2.2.8: Not Responding.
Checking IP 4.2.2.9: Responding. Host is up.
Checking IP 4.2.2.10: Not Responding.
Checking IP 4.2.2.11: Not Responding.
Checking IP 4.2.2.12: Responding. Host is up.
Checking IP 4.2.2.13: Not Responding.
Checking IP 4.2.2.14: Responding. Host is up.
Hosts up: 9

```