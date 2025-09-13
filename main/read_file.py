import pyshark
from constants import SAVE_PATH

def read_packets_from_file(device_ip):
    cap = pyshark.FileCapture(SAVE_PATH)

    for packet in cap:
        if "IP" in packet:
            if packet.ip.dst == device_ip:
                print(f"IP Source: {packet.ip.src} -> IP Dest: {packet.ip.dst}")

    cap.close()

