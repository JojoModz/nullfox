def xor_encrypt(data, key):
    if not key:
        raise ValueError("Key cannot be empty 💀")

    key_bytes = key.encode()
    return bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])