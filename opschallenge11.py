# Refrenced from Code Fellows Github. Incomplete!

from scapy.all import Ether, IP, sniff, ARP, sr1, ICMP, TCP

my_frame = Ether() / IP()

print(my_frame)
print('-' * 80)
# print(my_frame.show())
# print(my_frame.summary())
print('-' * 80)