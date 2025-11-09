# imports
from scapy.all import *
import nmap

def netowrk_scan(network_ip, netmask='24', timeout=5, iface='eth1'):
    ether_header = Ether(src = '00:00:00:11:22:33', dst="FF:FF:FF:FF:FF:FF")
    arp_header = ARP(pdst=f"{network_ip}/{netmask}")

    frame = ether_header / arp_header

    ans, unans = srp(frame, timeout=timeout, verbose=False) # pune iface
    
    for send, received in ans:
        print(f"{received[ARP].pdst} is at {received[Ether].src}")

    print(f"Summary: answered {len(ans)}, unanswered {len(unans)}")



