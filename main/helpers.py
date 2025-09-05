def convert_subnetMask_to_slash(subnet_mask):
    mask = 0

    for octet in subnet_mask.split("."):
        mask += bin(int(octet)).count("1")

    return mask



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