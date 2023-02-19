from scapy.all import *

def analyzer(pkt):
    if pkt.haslayer(TCP):
        print("TCP Packet! ...")
    if pkt.haslayer(UDP):
        print("UDP Packet! ...")
    if pkt.haslayer(ICMP):
        print("ICMP Packet! ...")    
       


print("************ Started *************")
sniff(iface="Wi-Fi", prn=analyzer)