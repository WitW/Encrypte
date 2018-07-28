# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 20:26
# @Author  : WitW
# @Aphorisms : Life is a struggle
# @Target : des加密

from Cryptodome.Cipher import DES

key = b"12345676"


def pad(text):
    while len(text) % 8 != 0:
        text += " "
    return text


des = DES.new(key, DES.MODE_ECB)  # 创建一个DES实例 key为8位 加密内容为8的倍数
text = 'hello world'
padded_text = pad(text)
print(padded_text)
encrypted_text = des.encrypt(padded_text.encode('utf-8'))
print(encrypted_text)
plain_text = des.decrypt(encrypted_text).decode().rstrip(' ')
print(plain_text)
