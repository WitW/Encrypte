# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 22:22
# @Author  : WitW
# @Aphorisms : Life is a struggle
# @Target : socket聊天程序

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print("连接地址：", addr)
    # c.send('开始对话<<<'.encode())
    # data = c.recv(1024).decode()
    # print(data.encode())
    # c.close()
    while True:
        try:
            data = c.recv(1024)
            if not data:
                break
            print("server 收到的数据",data.decode())
            response = input("回复>>").strip()
            c.send(response.encode())
            print("successfully send")
        except ConnectionResetError:
            break
    c.close()
s.close()