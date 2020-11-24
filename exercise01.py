"""
练习： 基于http_test完成
将网页 zhihu.html 文件以响应体发送给浏览器
"""
from socket import *


# 发送响应
def send_response(c, filename):
    with open(filename) as f:
        data = f.read()
    # 组织响应格式
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type:text/html\r\n"
    response += "\r\n"
    response += data

    c.send(response.encode())  # 发送给浏览器


# 接收浏览器的请求进行打印
def recv_request(c):
    data = c.recv(1024 * 10)  # 接收到了HTTP请求
    print(data.decode())


def main():
    # 　TCP
    s = socket()
    s.bind(("0.0.0.0", 8800))
    s.listen(5)

    while True:
        c, addr = s.accept()  # 连接了客户端（浏览器）
        print("Connect from", addr)
        recv_request(c)  # 接收请求
        send_response(c, "./zhihu.html")  # 发送响应
        c.close()

    s.close()


if __name__ == '__main__':
    main()
