from identify_attacks import listen_arp_spoofing_call
from helpers import  find_interfaces, get_network_ip, binary_to_decimanal_address

def display_available_interfaces(interfaces):
    print("Available interfaces")

    for index in range(len(interfaces)):
        interf = interfaces[index]
        
        if index == 0:
            device_IP = interf[1]
            netmask = interf[2]
            current_interface_name = interf[0]

        print(f"{'=> ' if index == 0 else ""} {interf[0]}: {interf[1]} {interf[2]}")


while True:
    interfaces = find_interfaces()

    device_IP = interfaces[0][1]
    netmask = interfaces[0][2]
    current_interface_name = interfaces[0][0]

    # Display available interfaces
    if len(interfaces) == 0:
        print("No interfaces found! ;(\nPlease try again later..")
        
        break 
    else:
        display_available_interfaces(interfaces)
        network_ip = get_network_ip(device_IP, netmask)

    # --- User UI Menu
    print("\nWhat u wanna do?\n[1] -> Listen for ARP Spoofing")
    option = input("Option: ")

    if option == "1":
        listen_arp_spoofing_call(network_ip, netmask, current_interface_name)
    else:
        print("invalid")

