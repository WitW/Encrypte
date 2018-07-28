# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 22:29
# @Author  : WitW
# @Aphorisms : Life is a struggle
# @Target : socket聊天程序

import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
addr = (host, port)
s.connect(addr)
print("连接成功,开始对话")
while True:
    msg = input().strip()
    if not msg:
        continue
    s.send(msg.encode())
    print(s.recv(1024).decode())
s.close()
