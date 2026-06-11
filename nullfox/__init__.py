"""
NullFox Cryptographic Suite - Top-Level Namespace Shortcut Router
Exposes the core 0.7.0 API directly from the underlying src/Python layer.
"""

from .src.Python.engine_backend import (
    encrypt_string,
    decrypt_string,
    encrypt_file,
    decrypt_file
)

from .src.Python.wrapper import (
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