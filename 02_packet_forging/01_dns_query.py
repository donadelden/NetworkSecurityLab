from scapy.all import *
conf.L3socket=L3RawSocket

dns_query = IP(dst="8.8.8.8") / UDP(sport=RandShort(), dport=53) / DNS(rd=1, qd=DNSQR(qname="www.univr.it"))

response = sr1(dns_query)

if response:
    print(response.show())
