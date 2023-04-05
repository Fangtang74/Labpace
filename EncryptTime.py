import hashlib
import time
import os
from Crypto.Cipher import AES
from pypuf.simulation import LightweightSecurePUF
from pypuf.simulation import InterposePUF
from pypuf.io import random_inputs

# pip3 install pypuf
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
print("异或加密的时间为：", total_time)
