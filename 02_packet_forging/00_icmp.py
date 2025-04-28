from scapy.all import *
conf.L3socket=L3RawSocket

target = "8.8.8.8"

ip = IP(dst=target)

pkt = ip / ICMP(id=0x1234)

print(pkt)
sr1(pkt)
