# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 22:01
# @Author  : WitW
# @Aphorisms : Life is a struggle
# @Target : RSA加密

import rsa
from binascii import b2a_hex, a2b_hex

"""
公钥加密算法，一种非对称密码算法
公钥加密，私钥解密
3个参数：
rsa_n， rsa_e，message
rsa_n, rsa_e 用于生成公钥
message： 需要加密的消息
"""


class rsacrypt:

    def __init__(self, pubkey, prikey):
        self.pubkey = pubkey
        self.prikey = prikey

    def encrypt(self, text):
        ciphertext = rsa.encrypt(text.encode(), self.pubkey)
        return b2a_hex(ciphertext)

    def decrypt(self, text):
        decrypt_text = rsa.decrypt(a2b_hex(text), self.prikey)
        return decrypt_text


if __name__ == "__main__":
    pubkey, prikey = rsa.newkeys(256)
    rs_obj = rsacrypt(pubkey, prikey)
    text = "hello"
    ency_text = rs_obj.encrypt(text)
    print(ency_text)
    print(rs_obj.decrypt(ency_text))
