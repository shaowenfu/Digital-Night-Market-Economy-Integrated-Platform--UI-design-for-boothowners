# 使用哈希函数计算
import hashlib


def sha256_hash(password):
    # 创建 SHA-256 哈希对象
    sha256_hash = hashlib.sha256()

    # 更新哈希对象的内容
    sha256_hash.update(password.encode('utf-8'))

    # 获取十六进制表示的哈希值
    hash_value = sha256_hash.hexdigest()

    return hash_value