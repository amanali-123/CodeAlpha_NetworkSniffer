from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    print("\n" + "="*50)
    print("📦 New Packet Captured!")
    
    if IP in packet:
        print(f"🔹 Source IP      : {packet[IP].src}")
        print(f"🔹 Destination IP : {packet[IP].dst}")
        print(f"🔹 Protocol       : {packet[IP].proto}")
        
        if TCP in packet:
            print(f"🔷 Protocol Name  : TCP")
            print(f"🔷 Source Port    : {packet[TCP].sport}")
            print(f"🔷 Dest Port      : {packet[TCP].dport}")
            
        elif UDP in packet:
            print(f"🟡 Protocol Name  : UDP")
            print(f"🟡 Source Port    : {packet[UDP].sport}")
            print(f"🟡 Dest Port      : {packet[UDP].dport}")
            
        elif ICMP in packet:
            print(f"🟢 Protocol Name  : ICMP (Ping)")

print("🚀 Network Sniffer Started...")
print("⏳ Capturing 10 packets... Please wait\n")

sniff(count=10, prn=packet_callback, store=0)

print("\n✅ Done! 10 Packets Captured Successfully!")