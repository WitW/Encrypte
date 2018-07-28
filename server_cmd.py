# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 23:12
# @Author  : WitW
# @Aphorisms : Life is a struggle
# @Target : socket简单的远程命令执行程序

import socket
import subprocess
import struct
import json


def cmd_exec(cmd):
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return stderr
    return stdout


IP_PORT = (socket.gethostname(), 12345)
sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.bind(IP_PORT)
sock_server.listen(5)
print("start<<<")
while True:
    conn, addr = sock_server.accept()
    print("连接地址：", addr)
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print("客户端命令:", data.decode("GBK"))
            res = cmd_exec(data.decode("GBK"))
            header = {
                'cmd':data.decode("GBK"),
                'res_size': len(res)
            }
            header_json = json.dumps(header)
            header_bytes = header_json.encode("utf-8")
            header = struct.pack('i', len(header_bytes))
            conn.send(header)
            conn.sendall(res)
        except ConnectionResetError:
            break
    conn.close()
sock_server.close()