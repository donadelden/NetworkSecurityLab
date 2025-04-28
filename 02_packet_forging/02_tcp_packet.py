from scapy.all import *

# target
target = "127.0.0.1"
tport = 80
TCP = TCP(sport=5555, dport=tport, flags="S")
ip = IP(dst=target)
payload = Raw(b"Hello World")

# packet
pkt = ip / TCP / payload

print(pkt)
send(pkt)
