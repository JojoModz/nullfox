"""
NullFox Encrypter Native Binary Interface
Handles cross-platform CFFI loading and symbol mapping for native C subroutines.
"""

import os
import sys
from cffi import FFI

ffi = FFI()

# Define the exact signatures present in the compiled C binary export table
ffi.cdef("""
    int nullfox_aes_encrypt(const unsigned char *plaintext, int plaintext_len, unsigned char *ciphertext, const unsigned char *key, const unsigned char *iv);
    int nullfox_aes_decrypt(const unsigned char *ciphertext, int ciphertext_len, unsigned char *plaintext, const unsigned char *key, const unsigned char *iv);
    int nullfox_file_encrypt(const char *input_path, const char *output_path, const unsigned char *key, const unsigned char *iv);
    int nullfox_file_decrypt(const char *input_path, const char *output_path, const unsigned char *key, const unsigned char *iv);
""")

def _resolve_binary_path() -> str:
    """Locates the platform-specific pre-compiled native machine library asset."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    if sys.platform.startswith("win"):
        return os.path.join(base_dir, "libnullfox_windows.dll")
    elif sys.platform.startswith("linux"):
        # Check for Android environment mapping overrides
        if "ANDROID_DATA" in os.environ:
            return os.path.join(base_dir, "libnullfox_android.so")
        return os.path.join(base_dir, "libnullfox_linux.so")
    else:
        raise OSError(f"Unsupported operating system runtime target environment: {sys.platform}")

# Load the native machine binary engine boundaries
_lib_path = _resolve_binary_path()
if not os.path.exists(_lib_path):
    raise FileNotFoundError(f"Critical System Fault: Native binary asset missing at target path: '{_lib_path}'")

_native_lib = ffi.dlopen(_lib_path)

def aes_encrypt_py(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    """Python wrapper for native block-level symmetric encryption."""
    if len(key) != 32:
        raise ValueError("Cryptographic Failure: AES-256 key constraint requires exactly 32 bytes.")
    if len(iv) != 16:
        raise ValueError("Cryptographic Failure: Initialization vector constraint requires exactly 16 bytes.")
        
    plaintext_len = len(plaintext)
    ciphertext = ffi.new("unsigned char[]", plaintext_len)
    
    result = _native_lib.nullfox_aes_encrypt(plaintext, plaintext_len, ciphertext, key, iv)
    if result != 0:
        raise RuntimeError(f"Native Engine Execution Failure: AES encryption routine returned fault code {result}")
        
    return ffi.unpack(ciphertext, plaintext_len)

def aes_decrypt_py(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    """Python wrapper for native block-level symmetric decryption."""
    if len(key) != 32:
        raise ValueError("Cryptographic Failure: AES-256 key constraint requires exactly 32 bytes.")
    if len(iv) != 16:
        raise ValueError("Cryptographic Failure: Initialization vector constraint requires exactly 16 bytes.")
        
    ciphertext_len = len(ciphertext)
    plaintext = ffi.new("unsigned char[]", ciphertext_len)
    
    result = _native_lib.nullfox_aes_decrypt(ciphertext, ciphertext_len, plaintext, key, iv)
    if result != 0:
        raise RuntimeError(f"Native Engine Execution Failure: AES decryption routine returned fault code {result}")
        
    return ffi.unpack(plaintext, ciphertext_len)

def file_encrypt_py(input_path: str, output_path: str, key: bytes, iv: bytes) -> int:
    """Python wrapper triggering native direct file encryption."""
    if len(key) != 32 or len(iv) != 16:
        raise ValueError("Cryptographic Failure: Absolute 32-byte key and 16-byte IV size constraints required.")
        
    c_input = ffi.new("char[]", input_path.encode('utf-8'))
    c_output = ffi.new("char[]", output_path.encode('utf-8'))
    
    return _native_lib.nullfox_file_encrypt(c_input, c_output, key, iv)

def file_decrypt_py(input_path: str, output_path: str, key: bytes, iv: bytes) -> int:
    """Python wrapper triggering native direct file decryption."""
    if len(key) != 32 or len(iv) != 16:
        raise ValueError("Cryptographic Failure: Absolute 32-byte key and 16-byte IV size constraints required.")
        
    c_input = ffi.new("char[]", input_path.encode('utf-8'))
    c_output = ffi.new("char[]", output_path.encode('utf-8'))
    
    return _native_lib.nullfox_file_decrypt(c_input, c_output, key, iv)