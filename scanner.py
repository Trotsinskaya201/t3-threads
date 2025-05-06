import socket
from threading import Thread

N = 2**16 - 1

for port in range(N):
    sock = socket.socket()
    try:
        print(port)
        sock.connect(('127.0.0.1', port))
        print("Порт", port, "открыт")
    except:
        continue
    finally:
        sock.close()