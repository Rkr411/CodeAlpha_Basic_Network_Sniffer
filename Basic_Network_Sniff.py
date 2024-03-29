import scapy.all as scapy

def sniff_packets(interface, count):
    print(f"Sniffing {count} packets on interface {interface}...")
    packets = scapy.sniff(iface=interface, count=count)
    return packets

def analyze_packets(packets):
    print("Analyzing captured packets...")
    for packet in packets:
        print(packet.summary())

def main():
    interface = input("Enter the interface to sniff: ")
    count = int(input("Enter the number of packets to sniff: "))
    
    captured_packets = sniff_packets(interface, count)
    analyze_packets(captured_packets)

if __name__ == "__main__":
    main()
