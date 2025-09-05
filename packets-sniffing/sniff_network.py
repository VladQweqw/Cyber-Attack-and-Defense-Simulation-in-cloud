import pyshark
from constants import SAVE_PATH

def sniff_packets():
    print("=-=-= Capture started =-=-=")

    capture = pyshark.LiveCapture(interface="\\Device\\NPF_{97828547-42FF-410D-9D7A-C73A9C2E53D6}", output_file=SAVE_PATH)
    # capture.sniff(timeout=5) # pe timp

    capture.sniff(packet_count=100)

    print(f"=-=-= Capture ended, file saved  at {SAVE_PATH} =-=-=")
