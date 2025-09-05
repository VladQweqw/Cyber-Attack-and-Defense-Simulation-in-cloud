from identify_attacks import listen_arp_spoofing_call

from constants import DEFAULT_NETWORK_IP, DEFAULT_SUBNET


while True:
    print("What u wanna do?\n[1] -> Listen for ARP Spoofing")
    option = input("Option: ")

    if option == "1":
        new_network = input(f"You want to change default network? ({DEFAULT_NETWORK_IP}):\n(y/N)")
        if(new_network):
            new_subnet = input(f"You want to change default subnet? ({DEFAULT_SUBNET}):\n(y/N)")

        if(new_network != ""):
            listen_arp_spoofing_call(new_network, new_subnet)
        else:
            listen_arp_spoofing_call(DEFAULT_NETWORK_IP, DEFAULT_SUBNET)
    else:
        print("invalid")

