from sniff_network import capture_live_packets
from helpers import convert_subnetMask_to_slash, is_IP_in_network, binary_to_decimanal_address

network_hosts = {}

def listen_arp_spoofing(packet, network_ip, subnet):
    ip_dest, ip_src = "", ""
    mac_dest, mac_src = "", ""

    # if packet type is arp requsest sau cv cu new mac for my ip, alert it sau cv si blocheaza trimitand tu alt arp req

    print(packet)

    if "IP" in packet:
        ip_dest = packet.ip.dst
        ip_src = packet.ip.src

        
    if "ETH" in packet:
        mac_dest = packet.eth.dst
        mac_src = packet.eth.src
        

    # print(f"IP Src: {ip_src}, IP Dest: {ip_dest}")
    # print(f"MAC Src: {mac_src}, MAC Dest: {mac_dest}\n")


def listen_arp_spoofing_call(network_ip, subnet, interface):
    decimal_ip = binary_to_decimanal_address(network_ip)
    print(f"Scanning network {decimal_ip}/{convert_subnetMask_to_slash(subnet)}")

    capture_live_packets(
        lambda packet: listen_arp_spoofing(packet, decimal_ip, subnet),
        interface
    )

