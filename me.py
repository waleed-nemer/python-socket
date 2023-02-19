from scapy.all import *


def analyzer(pkt):

    if pkt.haslayer(TCP):
        print("-------------------------")

        print("TCP Packet! ...")

        src_ip = pkt[IP].src

        dst_ip = pkt[IP].dst
        ########################

        mac_src = pkt.src

        mac_dst = pkt.dst
        ########################
        src_port = pkt.sport

        det_port = pkt.dport

        print("Src-IP :" + src_ip)

        print("Dst-IP :" + dst_ip)

        print("SRC-MAC :" + mac_src)

        print("DST-IP :" + mac_dst)

        print("SRC-PORT :" + str(src_port))

        print("DST-PORT :" + str(dst_port))
        print("-------------------------")


    if pkt.haslayer(UDP):
        print("-------------------------")

        print("UDP Packet! ...")

        src_ip = pkt[IP].src

        dst_ip = pkt[IP].dst
        ########################

        mac_src = pkt.src

        mac_dst = pkt.dst
        ########################
        src_port = pkt.sport

        det_port = pkt.dport

        print("Src-IP :" + src_ip)

        print("Dst-IP :" + dst_ip)

        print("SRC-MAC :" + mac_src)

        print("DST-IP :" + mac_dst)

        print("SRC-PORT :" + str(src_port))

        print("DST-PORT :" + str(dst_port))
        print("-------------------------")



print("************ Started *************")

sniff(iface="Wi-Fi", prn=analyzer)