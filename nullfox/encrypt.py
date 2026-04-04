import base64
from .utils import xor_encrypt

def encrypt_static(input_path, output_path, key):
    with open(input_path, "rb") as f:
        data = f.read()

    encrypted = xor_encrypt(data, key)
    encoded = base64.b64encode(encrypted)

    with open(output_path, "wb") as f:
        f.write(encoded)

    return True


def decrypt_static(input_path, output_path, key):
    with open(input_path, "rb") as f:
        data = f.read()

    decoded = base64.b64decode(data)
    decrypted = xor_encrypt(decoded, key)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(decrypted.decode("utf-8", errors="ignore"))
        
    
def decrypt_runtime(input_path, key):
    with open(input_path, "rb") as f:
        data = f.read()

    decoded = base64.b64decode(data)
    decrypted = xor_encrypt(decoded, key)

    return decrypted  # ⚔️ return bytes
    
  
def encrypt_file(input_path, output_path, key):
    return encrypt_static(input_path, output_path, key)

    return True