from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)


# 循环数据收发
while True:
    data = input("我：")
    if not data:
        break
    # 整个套接字创建连接操作都需要重新来
    tcp_socket = socket()
    tcp_socket.connect(ADDR)

    tcp_socket.send(data.encode())
    data = tcp_socket.recv(1024)
    print("小美说:",data.decode())

    tcp_socket.close()