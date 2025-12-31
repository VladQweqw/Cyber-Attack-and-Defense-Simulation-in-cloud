from scapy.all import *
import nmap

def network_scan(network_ip, netmask='24', timeout=2, iface='eth0', verbose=False, output=False):
    print(f"Scanning network on {iface}...")
    ether_header = Ether(dst="ff:ff:ff:ff:ff:ff")    
    arp_header = ARP(pdst=f"{network_ip}/{netmask}")
    frame = ether_header / arp_header

    ans, unans = srp(frame, timeout=timeout, verbose=False, iface=iface)

    if not verbose:
        for send, received in ans:
            print(f"=> {received[ARP].psrc} is at {received[Ether].src}")

        print(f"Summary: answered {len(ans)}, unanswered {len(unans)}")

    if output: 
        return ans


def port_scanner(target_ip, port_range='22-443'):
    print("Starting scanning ports...")
    nm = nmap.PortScanner()
    nm.scan(target_ip, port_range)

    target = nm[target_ip]

    # get device info
    device_hostname = target['hostnames'][0]['name'] or "No name"
    device_type = target['hostnames'][0]['type'] or "No Type"
    IPv4_address = target['addresses']['ipv4'] or "No IP"
    MAC_address = target['addresses']['mac'] or "No MAC"
    vendor = target['vendor'][MAC_address] or "No vendor"
    open_ports = target['tcp']

    # print info
    print(f"Hostname: {device_hostname}, {device_type}")
    print(f"IPv4: {IPv4_address}, MAC: {MAC_address}")
    print(f"Vendor: {vendor}")
    for port, state in open_ports.items():
        print(f"""Port: {port}, state: {state['state']}, name: {state['name']}, {state['product']}""")
