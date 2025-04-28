from scapy.all import *

print("Sniffing packets...")

def print_pkt(pkt):
    print(pkt.summary())

#pkt = sniff(filter='tcp', prn=print_pkt)
pkt = sniff(filter='icmp', prn=print_pkt, iface="lo")