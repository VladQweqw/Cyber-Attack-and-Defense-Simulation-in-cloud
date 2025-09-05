from sniff_network import capture_live_packets

def listen_arp_spoofing(packet):
    print(packet)

def listen_arp_spoofing_call():
    capture_live_packets(listen_arp_spoofing)

