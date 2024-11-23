from scapy.all import sniff, IP
import csv

def capture_packets(output_file, count=100):
    def packet_to_csv(packet):
        with open(output_file, 'a') as f:
            writer = csv.writer(f)
            if IP in packet:
                writer.writerow([packet[IP].src, packet[IP].dst, packet.proto, len(packet)])

    sniff(prn=packet_to_csv, count=count)

if __name__ == '__main__':
    capture_packets('data/network_data.csv')
