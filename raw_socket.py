import socket, sys
try:
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

except socket.error as e:
    print("Error occured....\n" + (e[0]))
    sys.exit()