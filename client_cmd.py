# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 23:24
# @Author  : WitW
# @Aphorisms : Life is a struggle
# @Target : socket简单的远程命令执行程序

import socket
import struct
import json

IP_PORT = (socket.gethostname(), 12345)
sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.connect(IP_PORT)
while True:
    msg = input("请输入命令:").strip()
    if not msg:
        continue
    sock_server.send(msg.encode("gbk"))

    header = sock_server.recv(4)
    header_size = struct.unpack('i', header)[0]
    print("收到报头长度:", header_size)
    header_json = sock_server.recv(header_size)
    header_dict = json.loads(header_json)
    print("收到报头内容:", header_dict)
    total_size = header_dict["res_size"]

    recv_size = 0
    recv_data = b''
    while recv_size < total_size:
        data = sock_server.recv(1024)
        recv_data += data
        recv_size += len(data)
        print("接收数据:",recv_data.decode("gbk", "ignore"))
sock_server.close()