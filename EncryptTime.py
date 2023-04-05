import hashlib
import time
import os
from Crypto.Cipher import AES
from pypuf.simulation import LightweightSecurePUF
from pypuf.simulation import InterposePUF
from pypuf.io import random_inputs
import numpy as np
import random

'''# pip3 install pypuf
# PUF过程
puf = LightweightSecurePUF(n=160, k=8, seed=1)
# puf = InterposePUF(n=160, k_up=8, k_down=8,  seed=1)
start_time = time.perf_counter()
puf.eval(random_inputs(n=160, N=160, seed=2))
end_time = time.perf_counter()
total_time = (end_time-start_time)*1000
print("PUF生成的时间为：", total_time)


# 随机数
start_time = time.perf_counter()
nonce = os.urandom(20)
nonce_hex = nonce.hex()
end_time = time.perf_counter()
total_time = (end_time-start_time)*1000
print("随机数生成的时间为：", total_time)


# AES加密
def aes_encrypt(data, key):
    # 创建AES加密器
    aes = AES.new(key, AES.MODE_ECB)
    # 进行加密
    encrypted_data = aes.encrypt(data)
    return encrypted_data


data = os.urandom(32)
key = os.urandom(32)
start_time = time.perf_counter()
encrypted_data = aes_encrypt(data, key)
end_time = time.perf_counter()
total_time = (end_time-start_time)*1000
# 打印加密后的数据
print("AES加密的运行时间为：", total_time)


# 哈希运算
str = os.urandom(32)
start_time = time.perf_counter()
hashlib.sha1(str).hexdigest()
end_time = time.perf_counter()
total_time = (end_time-start_time)*1000
print("哈希运算的时间为：", total_time)


# 异或加密

def xor_encrypt(data, key):
    # 将32字节数据和32字节密钥按字节逐位进行XOR运算
    encrypted = bytearray()
    for i in range(len(data)):
        encrypted.append(data[i] ^ key[i % len(key)])
    return encrypted


# 生成32字节随机数据和密钥
data = os.urandom(32)
key = os.urandom(32)
# 加密数据并打印结果
start_time = time.perf_counter()
encrypted_data = xor_encrypt(data, key)
end_time = time.perf_counter()
total_time = (end_time-start_time)*1000
print("异或加密的时间为：", total_time)'''


def fuzzy(x):
    return x ^ random.randint(0, 255)


# 定义模糊提取器的重构函数
def de_fuzzy(y):
    return y ^ random.randint(0, 255)


# 原始数据
original_data = os.urandom(128)

# 模糊提取器的提取过程
fuzzy_data = []
start_time = time.perf_counter()
for byte in original_data:
    fuzzy_data.append(fuzzy(byte))
end_time = time.perf_counter()
print("模糊提取器的提取时间：", (end_time-start_time)*1000)

# 模糊提取器的重构过程
reconstructed_data = b''
start_time = time.perf_counter()
for byte in fuzzy_data:
    reconstructed_data += bytes([de_fuzzy(byte)])
end_time = time.perf_counter()
print("模糊提取器的重构时间：", (end_time-start_time)*1000)

data = os.urandom(40)
lst = []
for i in range(0, 1024):
    lst.append(i)
start_time = time.perf_counter()
random.shuffle(lst)  # 随机打乱列表
end_time = time.perf_counter()
print("随机洗牌的时间：", (end_time-start_time)*1000)

'''
# 运行时间计算
# UAV运行次数
num_aes = 0
num_xor = 1
num_rand = 2
num_puf = 1
num_hash = 5
# GS运行次数
aes = 0
xor = 1
rand = 1
hash = 5
other = 0
total_uav_time = 0.02646*num_xor+0.06135*num_hash + \
    0.01052*num_rand+2.06104*num_puf+0.82487*num_aes
total_gs_time = 0.00537*xor+0.00904*hash + \
    0.00358*rand+0.28915*aes+other
print("协议计算时间(ms)为：", total_uav_time+total_gs_time)'''
