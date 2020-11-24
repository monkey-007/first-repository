"""
tcp 套接字循环模型 2
重点代码 ！！！
"""
from socket import *
import re
# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听套接字
tcp_socket.listen(5)

def answer(data):
    with open("char.txt","r") as f:
        for line in f.readlines():
            result = re.findall("(\w+)\s+(.+)",line)
            if data == result[0][0]:
                return result[0][1]
    return "我还小,不知道呢！"

# 循环等待处理客户端
while True:
    connfd,addr = tcp_socket.accept()

    data = connfd.recv(1024)
    print("用户问：",data.decode())
    result = answer(data.decode())
    connfd.send(result.encode())

    connfd.close()



# 关闭
tcp_socket.close()


