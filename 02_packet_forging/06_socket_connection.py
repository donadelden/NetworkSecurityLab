import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind to an address and port
sock.bind(('', 1337))  

# listen for max = 5 connections
sock.listen(5)

# accept a connection
print("Waiting for a connection...")
sock, addr = sock.accept()
# print info about the connection
print("Got connection from", addr)

# close the socket
sock.close()