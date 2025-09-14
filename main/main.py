from identify_attacks import listen_arp_spoofing_call
from helpers import  find_main_interfaces, get_network_ip, binary_to_decimanal_address

print(
    binary_to_decimanal_address("11000000101010001010010100000000")
)

while True:
    interfaces = find_main_interfaces()

    device_IP = ""
    netmask = ""
    current_interface_name = ''

    print("Available interfaces")
    for index in range(len(interfaces)):
        interf = interfaces[index]

        if index == 0:
            device_IP = interf[1]
            netmask = interf[2]
            current_interface_name = interf[0]

        print(f"{'=> ' if index == 0 else ""} {interf[0]}: {interf[1]} {interf[2]}")

    network_ip = get_network_ip(device_IP, netmask)

    print("\nWhat u wanna do?\n[1] -> Listen for ARP Spoofing")
    option = input("Option: ")

    if option == "1":
        listen_arp_spoofing_call(network_ip, netmask, current_interface_name)
    else:
        print("invalid")

