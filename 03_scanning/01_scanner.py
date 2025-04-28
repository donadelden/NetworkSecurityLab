import socket

TARGET = "scanme.nmap.org"

for port in range(1, 100):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((TARGET, port))
        print(f"Port {port} is open")
    except:
        pass