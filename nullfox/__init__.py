"""
NullFox Cross-Platform Native Encryption Suite
An enterprise-grade, high-performance compilation toolkit providing optimized
AES-256 and SHA-256 cryptographic routines across Windows, Linux, and Android targets.
"""

# Explicitly expose top-level public API functions for developers
from nullfox.encrypt import (
    encrypt_file,
    decrypt_file
)
from nullfox.utils import xor_encrypt

# Global Package Component Metadata Tracking
__version__ = "0.6.0"
__author__ = "JojoModz"
__license__ = "MIT"

# Control explicit package namespace exports
__all__ = [
    "encrypt_file",
    "decrypt_file",
    "xor_encrypt"
]