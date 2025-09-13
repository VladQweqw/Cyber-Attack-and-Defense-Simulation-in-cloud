import pyshark
from constants import SAVE_PATH
from read_file import read_packets_from_file

def sniff_packets(interface):
    print("=-=-= Capture started =-=-=")

    capture = pyshark.LiveCapture(interface=interface, output_file=SAVE_PATH)
    # capture.sniff(timeout=5) # pe timp

    capture.sniff(packet_count=100)

    print(f"=-=-= Capture ended, file saved  at {SAVE_PATH} =-=-=")

    capture.close()


def capture_live_packets(cb, interface):
    capture = pyshark.LiveCapture(interface=interface)
    for raw_packet in capture.sniff_continuously():
        try:
            cb(raw_packet)
        except Exception as e:
            print('Error ' + e)
