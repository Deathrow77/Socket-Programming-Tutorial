import sys, socket
host = "127.0.0.1"
port = 3000
buffer_size = "1024"
try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error as e:
    print(e)

tcp_socket.bind((host, port))
tcp_socket.listen(2)
print("Listening .... \n")
while True:
    connection, address = tcp_socket.accept()
    print("Connection Established !! \n")
    print(address)
    data = connection.recv(1024)
    print("Data : ", data)
    connection.close()
tcp_socket.close()
