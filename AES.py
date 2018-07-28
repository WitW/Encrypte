# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 20:39
# @Author  : WitW
# @Aphorisms : Life is a struggle
# @Target : AES高级加密

from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex

"""
1、密钥扩展（KeyExpansion），
2、初始轮（Initial Round），
3、重复轮（Rounds），每一轮又包括：SubBytes、ShiftRows、MixColumns、AddRoundKey，
4、最终轮（Final Round），最终轮没有MixColumns。
"""


key = "12345678"  # 秘钥，需要将字符转为字节


def pad(text):
    # 加密内容需要为*16位字符
    while len(text) % 16 != 0:
        text += " "
    return text


def pad_key(key):
    # 秘钥加密需要秘钥位16位
    while len(key) % 16 != 0:
        key += " "
    return key


aes = AES.new(pad_key(key).encode(), AES.MODE_ECB)  # AES对象
text = "hello"
encrypted_text = aes.encrypt(pad(text).encode())
print(encrypted_text)
encrypted_text_hex = b2a_hex(encrypted_text)
print(encrypted_text_hex)
de = str(aes.decrypt(a2b_hex(encrypted_text_hex)), encoding='utf-8', errors='ignore')
print(de)
