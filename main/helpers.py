def convertSubnetMaskToSlash(subnet_mask):
    mask = 0

    for octet in subnet_mask.split("."):
        mask += bin(int(octet)).count("1")

    return mask
    
