from scapy.all import *

conf.L3socket = L3RawSocket # may resolve some issues when sending packets in Linux 

TARGET = "scanme.nmap.org" 

for port in range(1, 100):
    pkt = IP(dst=TARGET)/TCP(dport=port, sport=RandShort(), flags="S")  # SYN
    response = sr1(pkt, timeout=2, verbose=0)
    
    if response is not None and response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:  # SYN-ACK
            print(f"Port {port} is open")
            # Send RST to close the connection
            send(IP(dst=TARGET)/TCP(dport=port, flags="R"), verbose=0)
        elif response.getlayer(TCP).flags == 0x14:  # RST-ACK
            pass # port closed
    else:
        pass # no response, port filtered
