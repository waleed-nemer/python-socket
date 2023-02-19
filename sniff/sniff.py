from scapy.all import *

def analyzer(pkt):
    print("new packet....")
    print("------------")


print("************ Started *************")


sniff(iface="Wi-Fi", prn=analyzer)