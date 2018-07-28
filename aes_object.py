# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 20:52
# @Author  : WitW
# @Aphorisms : Life is a struggle
# @Target : AES面向对象方式

from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex

AES_LENGTH = 16


class prpcrypt:

    def __init__(self, key):
        self.key = key
        self.aes = AES.new(self.pad(key).encode(), AES.MODE_ECB)

    def pad(self, content):
        # 补齐内容被16整除
        while len(content) % AES_LENGTH != 0:
            content += " "
        return content

    def encrypt(self, text):
        # 加密
        ciphertext = self.aes.encrypt(self.pad(text).encode())
        return b2a_hex(ciphertext)

    def decrypt(self, text):
        # 解密
        plain_text = self.aes.decrypt(a2b_hex(text)).decode()
        return plain_text.rstrip(" ")


pc = prpcrypt("12345")
e = pc.encrypt("hello world")
d = pc.decrypt(e)
print(e, d)
