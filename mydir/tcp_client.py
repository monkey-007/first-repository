from socket import *

ADDR = ("127.0.0.1", 8877)

tcp_scoket = socket()
tcp_scoket.connect(ADDR)

while True:
    data = input(">>>")
    # if not data:
    #     break
    if data == "##":
        break
    tcp_scoket.send(data.encode())
    data = tcp_scoket.recv(1024)
    print("From sever:", data.decode())

tcp_scoket.close()
