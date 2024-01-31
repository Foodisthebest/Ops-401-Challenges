import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="opschallenge12",
        description="Network scanning tool using Python and Scapy.",
        epilog="Thanks for using %(prog)s! :)",
    )
    parser.add_argument(
        "-T", 
        "--TCP",
        action="store_true", help="TCP Port Range Scanner mode"
    )
    parser.add_argument(
        "-I",
        "--ICMP",
        action="store_true", help="ICMP Ping Sweep mode"
    )
    parser.add_argument(
        "-i",
        "--ip_address",
        type=str,
    )
    parser.add_argument(
        "-s",
        "--start_port",
        type=int,
        required=False,
        help="Start Port",
    )
    parser.add_argument(
        "-e",
        "--end_port",
        type=int,
        required=False,
        help="End Port",
    )
    parser.add_argument(
        "-P",
        "--ping_range",
        type=str,
        required=False,
        help="IP Range Ex: 10.0.0.0/24",
    )

    return parser.parse_args()
