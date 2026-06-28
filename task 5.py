from scapy.all import rdpcap, IP, TCP, UDP

pcap_file = input("Enter the PCAP file name: ")

try:
    packets = rdpcap(pcap_file)

    print("Total Packets:", len(packets))

    for i, packet in enumerate(packets, start=1):
        print("\nPacket", i)

        if IP in packet:
            print("Source IP      :", packet[IP].src)
            print("Destination IP :", packet[IP].dst)
            print("Protocol       :", packet[IP].proto)

        if TCP in packet:
            print("Transport      : TCP")
        elif UDP in packet:
            print("Transport      : UDP")

        if packet.payload:
            print("Payload:")
            print(packet.payload)

except FileNotFoundError:
    print("PCAP file not found.")
except Exception as e:
    print("Error:", e)