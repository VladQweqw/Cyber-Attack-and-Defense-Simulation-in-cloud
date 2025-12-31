import core.utils.attacks as attacks
import core.utils.tools as tools

import psutil
import ipaddress

class Attacker:
    interfaces = []
    active_interface = {}

    logo = r""" 
     ___           ____                 _             _   _             
    |_ _|__ _ _ __|  _ \ ___ _ __   ___| |_ _ __ __ _| |_(_) ___  _ __  
     | |/ _` | '__| |_) / _ \ '_ \ / _ \ __| '__/ _` | __| |/ _ \| '_ \ 
     | | (_| | |  |  __/  __/ | | |  __/ |_| | | (_| | |_| | (_) | | | |
    |___\__, |_|  |_|   \___|_| |_|\___|\__|_|  \__,_|\__|_|\___/|_| |_|
        |___/                                                           
                                                              
        """

    attack_options = {
        "Tools": {
            "1": "Network Scan",
            "2": "Port Scanner",
            "3": "Device Info",
        },
        "Attacks": {
            "4": "ARP Spoofing",
            "5": "ARP Spoofing (MIMT)",
            "6": "DHCP Starvation", 
            "7": "DHCP Spoofing",
            "8": "IP Spoofing",
            "9": "DNS Poisoning",
        },
        "Command": {
            "exit": "To close the program"
        }
    }

    def __init__(self):
        pass

    def ask_user_option(self):
        opt = input("Choose an option:\n> ")

        return opt

    def display_options(self):
        for opt_type, opt_dict in self.attack_options.items():
            print(f"== {opt_type} ==")
            for number, value in opt_dict.items():
                print(f"= [{number}] {value}")

            print()

    def displayInterfaces(self):
        count = 1

        for iface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family.name == 'AF_INET':
                    network = ipaddress.IPv4Network(f"{addr.address}/{addr.netmask}", strict=False)

                    # create a list of interfaces
                    self.interfaces.append({
                        "interface": iface,
                        'network_ip': network.network_address,
                        'host_ip': addr.address,
                        'netmask': network.netmask,
                        'netprefix': network.prefixlen,
                        'formatted': network,
                    })

                    # print them
                    print(f"= [{count}] {iface}: {network}")
            
            count += 1

    def select_target(self):
        tools.network_scan()

    def run_attack(self, option):
        typeOf = 'Tools'
        if int(option) > len(self.attack_options['Tools']):
            typeOf = 'Attacks'
    
        print(f"Running {self.attack_options[typeOf][option]}")

        if option == '1':
            tools.network_scan(
                network_ip=self.active_interface['network_ip'], 
                netmask=self.active_interface['netprefix'],
                iface=self.active_interface['interface'])
        elif option == '2':
            tools.port_scanner()
        print("\n")

    def isOptionValid(self, user_option):
        valids = [
            str(opt) for opt in range(
                1, 
                int(list(self.attack_options['Attacks'].keys())[-1])
            )
        ]

        # concat 2 lists
        # list of commands
        valids = valids + list(self.attack_options['Command'].keys())

        return user_option in valids

    def interface_menu(self):
        print(self.logo)
        print("== Interfaces ==")
        self.displayInterfaces()
        print()

        user_option = int(self.ask_user_option())

        while(user_option > len(self.interfaces) or user_option < 0):
            print("Invalid option")
            user_option = int(self.ask_user_option())

        # get the index - 1 interface
        self.active_interface = self.interfaces[user_option - 1]

    def menu(self):
        print(self.logo)

        print("======>")
        print(f"Active interface: {self.active_interface['formatted']}")
        print("======>")

        print("Choose an option: ")
        self.display_options()

        user_option = self.ask_user_option()

        while user_option != 'exit':
            if not self.isOptionValid(user_option):
                print("=== Invalid Option ===\n")
            else:
                self.run_attack(user_option)
                input("<enter> to continue")

            self.display_options()
            user_option = self.ask_user_option()

        print("\n Bye!")

    def run(self):
        self.interface_menu()
        self.menu()