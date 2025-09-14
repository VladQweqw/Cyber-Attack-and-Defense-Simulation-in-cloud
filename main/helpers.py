import psutil

# Convert mask from bits to /24
def convert_subnetMask_to_slash(subnet_mask):
    mask = 0

    # split then count their 1's
    for octet in subnet_mask.split("."):
        mask += bin(int(octet)).count("1")

    return mask

# function to calculate network IP from an IP and subnet
def get_network_ip(host_ip, subnet_mask):
    host_ip_bin = convert_IP_to_binary(host_ip) # we need them in 11010101 format
    subnet_bin = convert_IP_to_binary(subnet_mask)

    network_ip_binary = "" # host add as binary
    for idx in range(32):
        # iterate over the 32 concrete length bits

        # add 1 if the subnet is 1, or 0 ( logical AND )
        if (host_ip_bin[idx] == subnet_bin[idx]) and host_ip_bin[idx] == "1":
            network_ip_binary += "1"
        else:
            network_ip_binary += "0"
            
    return network_ip_binary

def binary_to_decimal(binary_value):
    dec_val = 0
    # in order to not reverse the binary_value, we start with the "end", 2^7, 2^6 so on
    exponent = len(binary_value) - 1

    for digit in binary_value:
        # if the digit is 1 we add
        if digit == "1":
            dec_val += pow(2, exponent)

        # we decrese the exponent no matter
        exponent -= 1

    return dec_val


def binary_to_decimanal_address(ip_binary):
    a = ip_binary[:8] # first section and so on, 32 bits so we split the address by 4 section of 8 bits
    b = ip_binary[8:16]
    c = ip_binary[16:24]
    d = ip_binary[24:]

    # return add as string 101010101 => 192.168.1.10
    return f"{binary_to_decimal(a)}.{binary_to_decimal(b)}.{binary_to_decimal(c)}.{binary_to_decimal(d)}"

# find all IPv4 addresses
def find_interfaces():
    # store interfaces
    addresses = []

    # iterate over all interfaces
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            # if ip is IPv4
            if addr.family == 2:
                # add only interfaces that i need WiFi / Ethernet,
                if interface == "Wi-Fi" or interface == "Ethernet":
                    addresses.append(
                        (interface, addr.address, addr.netmask)
                    )
                    

    return addresses


def convert_IP_to_binary(ip):
    new_ip = ""
    
    for octet in ip.split("."):
        octet = int(octet)
        n = 7
        binary_octet = ""

        while(octet >= 0 and n >= 0):
            power = 2 ** n

            if octet - power >= 0:
                octet -= power
                binary_octet += "1"
            else:
                binary_octet += "0"

            n -= 1
        
        new_ip += binary_octet

    return new_ip

def is_IP_in_network(host_ip, network_ip, subnet_mask):
    netowrk_bits = convert_subnetMask_to_slash(subnet_mask)
    
    host_ip_bin = convert_IP_to_binary(host_ip)
    netowrk_ip_bin = convert_IP_to_binary(network_ip)
    
    for bit in range(0, netowrk_bits):
        if host_ip_bin[bit] != netowrk_ip_bin[bit]: return False

    return True