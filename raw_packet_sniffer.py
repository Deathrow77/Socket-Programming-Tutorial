import socket, sys, struct
try:
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))
except socket.error as e:
    print(e)
    sys.exit()
raw_socket.bind(("127.0.0.1", 3000))
while True:
    packet = raw_socket.recvfrom(2048)
    #print(packet)
    ethernet_header = packet[0][:14]
    eth_header = struct.unpack("!6s6s2s", ethernet_header)
    print("Destination : " + binascii.hexlify(eth_header[0]) + "\n Source : " + binascii.hexlify(eth_header[1])+ "\n Type : " + binascii.hexlify(eth_header[2]))
