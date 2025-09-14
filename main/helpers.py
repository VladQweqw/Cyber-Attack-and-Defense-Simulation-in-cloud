import psutil

def convert_subnetMask_to_slash(subnet_mask):
    mask = 0

    for octet in subnet_mask.split("."):
        mask += bin(int(octet)).count("1")

    return mask


def get_network_ip(host_ip, subnet_mask):
    host_ip_bin = convert_IP_to_binary(host_ip)
    subnet_bin = convert_IP_to_binary(subnet_mask)

    network_ip = ""
    for idx in range(32):
        if (host_ip_bin[idx] == subnet_bin[idx]) and host_ip_bin[idx] == "1":
            network_ip += "1"
        else:
            network_ip += "0"
            
    return network_ip

def binary_to_decimal(binary_value):
    dec_val = 0
    exponent = len(binary_value) - 1

    for digit in binary_value:
        if digit == "1":
            dec_val += pow(2, exponent)

        exponent -= 1

    return dec_val

def binary_to_decimanal_address(ip_binary):
    a = ip_binary[:8]
    b = ip_binary[8:16]
    c = ip_binary[16:24]
    d = ip_binary[24:]

    return f"{binary_to_decimal(a)}.{binary_to_decimal(b)}.{binary_to_decimal(c)}.{binary_to_decimal(d)}"


def find_main_interfaces():
    interfaces = find_interfaces()
    result = []

    for interf in interfaces:
        if interf[0] == "Wi-Fi" or interf[0] == "Ethernet":
            result.append(interf)
            continue
    
    return result

def find_interfaces():
    addresses = []

    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == 2:
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