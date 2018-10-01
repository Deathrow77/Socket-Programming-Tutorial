import socket, sys
host = "127.0.0.1"
port = 3000
buffer_size = "1024"
msg = b'Socket Connected!!'
try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Error occured while creation of socket...\n")
    print(e)
    sys.exit()
tcp_socket.connect((host, port))
try:
    tcp_socket.send(msg)
except socket.error as e:
    print(e)
    sys.exit()
