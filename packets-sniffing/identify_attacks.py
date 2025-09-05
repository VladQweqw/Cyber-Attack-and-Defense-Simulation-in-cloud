from sniff_network import capture_live_packets

def listen_arp_spoofing(packet):
    ip_dest, ip_src = "", ""
    mac_dest, mac_src = "", ""
   

    if "IP" in packet:
        ip_dest = packet.ip.dst
        ip_src = packet.ip.src
    if "ETH" in packet:
        mac_dest = packet.eth.dst
        mac_src = packet.eth.src

    print(
        ip_src,
        ip_dest,
        mac_dest,
        mac_src
    )
    

def listen_arp_spoofing_call():
    capture_live_packets(listen_arp_spoofing)

