from identify_attacks import listen_arp_spoofing_call

while True:
    print("What u wanna do?\n[1] -> Listen for ARP Spoofing")
    option = input("Option: ")

    if option == "1":
        listen_arp_spoofing_call()
    else:
        print("invalid")
