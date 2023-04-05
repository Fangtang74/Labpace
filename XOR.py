import os
import time


def xor_encrypt(data, key):
    # 将32字节数据和32字节密钥按字节逐位进行XOR运算
    start_time = time.perf_counter()
    encrypted = bytearray()
    for i in range(len(data)):
        encrypted.append(data[i] ^ key[i % len(key)])
    end_time = time.perf_counter()
    return encrypted, (end_time-start_time)*1000


# 生成32字节随机数据和密钥
data = os.urandom(128)
key = os.urandom(128)

# 打印原始数据和密钥
print("原始数据：", data.hex())
print("密钥：", key.hex())

# 加密数据并打印结果
encrypted_data, total_time = xor_encrypt(data, key)
print("加密后数据：", encrypted_data.hex())
print("运行时间：", total_time)
