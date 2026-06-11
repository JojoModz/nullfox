"""
NullFox Encryption Suite - High-Level Hybrid API Backend
Implements adaptive input parsing, strict validation loops, and armored
in-memory secret key scrubbing utilizing the native CFFI backend bridges.
"""

import os
from .wrapper import ffi, aes_encrypt_py, aes_decrypt_py, encrypt_file as file_encrypt_py, decrypt_file as file_decrypt_py

def _zero_memory_buffer(target) -> None:
    """
    Overwrites the sensitive content inside mutable buffers.
    Ensures secret key blocks are zero-stamped from RAM immediately after use.
    """
    if target is None:
        return
    if isinstance(target, bytearray):
        try:
            c_ptr = ffi.from_buffer("char[]", target)
            for i in range(len(target)):
                c_ptr[i] = b'\x00'
        except Exception:
            for i in range(len(target)):
                target[i] = 0


def _normalize_crypto_params(key, iv) -> tuple:
    """
    Normalizes incoming types into mutable bytearrays for in-flight memory security.
    Strictly enforces that credentials must be provided.
    """
    if key is None:
        raise ValueError("NullFox Error: Key is a required parameter and cannot be None.")
    if iv is None:
        raise ValueError("NullFox Error: IV is a required parameter and cannot be None.")

    # 1. Process 32-Byte AES Key
    if isinstance(key, str):
        try:
            raw_key = bytearray(bytes.fromhex(key))
        except ValueError:
            raise ValueError("NullFox Error: Provided custom Key string is not a valid hex block.")
    elif isinstance(key, (bytes, bytearray)):
        raw_key = bytearray(key)
    else:
        raise TypeError("NullFox Error: Key must be a hex string, raw bytes, or bytearray.")

    # 2. Process 16-Byte Initialization Vector
    if isinstance(iv, str):
        try:
            raw_iv = bytearray(bytes.fromhex(iv))
        except ValueError:
            raise ValueError("NullFox Error: Provided custom IV string is not a valid hex block.")
    elif isinstance(iv, (bytes, bytearray)):
        raw_iv = bytearray(iv)
    else:
        raise TypeError("NullFox Error: IV must be a hex string, raw bytes, or bytearray.")

    # Strict length constraints enforcement
    if len(raw_key) != 32:
        _zero_memory_buffer(raw_key)
        _zero_memory_buffer(raw_iv)
        raise ValueError(f"NullFox Error: Key constraint violation. Expected 32 bytes, got {len(raw_key)}.")
    if len(raw_iv) != 16:
        _zero_memory_buffer(raw_key)
        _zero_memory_buffer(raw_iv)
        raise ValueError(f"NullFox Error: IV constraint violation. Expected 16 bytes, got {len(raw_iv)}.")

    return raw_key, raw_iv


def encrypt_string(plaintext: bytes, key: str | bytes, iv: str | bytes) -> tuple:
    """
    Encrypts a raw byte string directly in system memory space.
    Returns: (ciphertext_bytes, key_bytes, iv_bytes)
    """
    if not isinstance(plaintext, (bytes, bytearray)):
        raise TypeError("NullFox Error: Plaintext must be submitted as raw bytes or bytearray.")
    
    raw_key = None
    raw_iv = None
    try:
        raw_key, raw_iv = _normalize_crypto_params(key, iv)
        ciphertext = aes_encrypt_py(plaintext, bytes(raw_key), bytes(raw_iv))
        safe_key = bytes(raw_key)
        safe_iv = bytes(raw_iv)
        return ciphertext, safe_key, safe_iv
    finally:
        _zero_memory_buffer(raw_key)
        _zero_memory_buffer(raw_iv)


def decrypt_string(ciphertext: bytes, key: str | bytes, iv: str | bytes) -> bytes:
    """
    Decrypts a ciphertext byte stream back to plaintext memory space.
    """
    if not isinstance(ciphertext, (bytes, bytearray)):
        raise TypeError("NullFox Error: Ciphertext must be submitted as raw bytes or bytearray.")

    raw_key = None
    raw_iv = None
    try:
        raw_key, raw_iv = _normalize_crypto_params(key, iv)
        return aes_decrypt_py(ciphertext, bytes(raw_key), bytes(raw_iv))
    finally:
        _zero_memory_buffer(raw_key)
        _zero_memory_buffer(raw_iv)


def encrypt_file(input_path: str, output_path: str, key: str | bytes, iv: str | bytes) -> tuple:
    """
    Encrypts a disk file using the native 64KB optimized C streaming engine.
    Returns: (key_bytes, iv_bytes)
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"NullFox Error: Source file target missing at: '{input_path}'")

    raw_key = None
    raw_iv = None
    try:
        raw_key, raw_iv = _normalize_crypto_params(key, iv)
        result = file_encrypt_py(input_path, output_path, bytes(raw_key), bytes(raw_iv))
        if result != 0:
            raise RuntimeError(f"NullFox C-Engine Fault: File encryption execution token failed with code {result}")
        return bytes(raw_key), bytes(raw_iv)
    finally:
        _zero_memory_buffer(raw_key)
        _zero_memory_buffer(raw_iv)


def decrypt_file(input_path: str, output_path: str, key: str | bytes, iv: str | bytes) -> bool:
    """
    Decrypts a disk file container utilizing the native C streaming engine.
    Accepts hex credentials strings directly from the console interface.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"NullFox Error: Encrypted target container missing at: '{input_path}'")

    raw_key = None
    raw_iv = None
    try:
        raw_key, raw_iv = _normalize_crypto_params(key, iv)
        result = file_decrypt_py(input_path, output_path, bytes(raw_key), bytes(raw_iv))
        if result != 0:
            raise RuntimeError(f"NullFox C-Engine Fault: File decryption execution token failed with code {result}")
        return True
    finally:
        _zero_memory_buffer(raw_key)
        _zero_memory_buffer(raw_iv)