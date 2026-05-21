"""
NullFox Encryption Suite File Processing Interfaces
Exposes optimized wrappers pointing to native C file processing subroutines.
"""

import os
from .wrapper import file_encrypt_py, file_decrypt_py

def encrypt_file(input_path: str, output_path: str, key: bytes, iv: bytes) -> bool:
    """
    Encrypts a file asset using the native C file processing engine.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"[Error] Source file target could not be resolved: {input_path}")
        
    result = file_encrypt_py(input_path, output_path, key, iv)
    if result != 0:
        raise RuntimeError(f"[Error] Native C file encryption engine failed with execution token: {result}")
        
    return True

def decrypt_file(input_path: str, output_path: str, key: bytes, iv: bytes) -> bool:
    """
    Decrypts a file asset using the native C file processing engine.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"[Error] Target encrypted container could not be resolved: {input_path}")
        
    result = file_decrypt_py(input_path, output_path, key, iv)
    if result != 0:
        raise RuntimeError(f"[Error] Native C file decryption engine failed with execution token: {result}")
        
    return True