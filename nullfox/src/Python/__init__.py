"""
NullFox Cryptographic Suite
Enterprise-grade AES-256-CBC and SHA-256 native toolkit.
"""

from .engine_backend import (
    encrypt_string,
    decrypt_string,
    encrypt_file,
    decrypt_file
)

from .wrapper import (
    generate_key,
    generate_iv,
    generate_key_pair,
    aes_encrypt_py,
    aes_decrypt_py
)

__version__ = "0.7.0"
__author__ = "NullFox"

__all__ = [
    "encrypt_string",
    "decrypt_string",
    "encrypt_file",
    "decrypt_file",
    "generate_key",
    "generate_iv",
    "generate_key_pair",
    "aes_encrypt_py",
    "aes_decrypt_py"
]