import core.utils.attacks as attacks
import core.utils.tools as tools

class Attacker:
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
            "4": "ARP Spoofing ",
            "5": "ARP Spoofing (MIMT)",
            "6": "DHCP Starvation", 
            "7": "DHCP Spoofing",
            "8": "IP Spoofing",
            "9": "DNS Poisoning",
            "10": "DNS Poisoning"
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

    def run_attack(self, option):
        typeOf = 'Tools'
        if int(option) > len(self.attack_options['Tools']):
            typeOf = 'Attacks'
    
        print(f"Running {self.attack_options[typeOf][option]}")
        tools.netowrk_scan("192.168.1.0", '24')

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

    def menu(self):
        print(self.logo)
        print("Choose an option: ")
        self.display_options()

        user_option = self.ask_user_option()

        while user_option != 'exit':
            if not self.isOptionValid(user_option):
                print("=== Invalid Option ===\n")
            else:
                self.run_attack(user_option)
                input("<enter> to continue")

            # ask the user again no matter
            self.display_options()
            user_option = self.ask_user_option()

        print("\n Bye!")

# start
attacker = Attacker()
attacker.menu()