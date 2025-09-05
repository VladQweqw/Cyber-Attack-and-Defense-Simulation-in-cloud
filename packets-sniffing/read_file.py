import pyshark
from constants import SAVE_PATH, MY_IP

def read_packets_from_file():
    cap = pyshark.FileCapture(SAVE_PATH)

    for packet in cap:
        if "IP" in packet:
            if packet.ip.dst == MY_IP:
                print(f"IP Source: {packet.ip.src} -> IP Dest: {packet.ip.dst}")