"""
NullFox Encryption Native Binary Interface
Handles cross-platform CFFI loading, strict validation, and symbol mapping 
for native C subroutines.
"""

import os
import sys
import secrets
from cffi import FFI

ffi = FFI()

# Map the exact C functions into the CFFI loader environment
ffi.cdef("""
    int nullfox_aes_encrypt(const unsigned char *plaintext, int plaintext_len, unsigned char *ciphertext, const unsigned char *key, const unsigned char *iv);
    int nullfox_aes_decrypt(const unsigned char *ciphertext, int ciphertext_len, unsigned char *plaintext, const unsigned char *key, const unsigned char *iv);
    int nullfox_file_encrypt(const char *input_path, const char *output_path, const unsigned char *key, const unsigned char *iv);
    int nullfox_file_decrypt(const char *input_path, const char *output_path, const unsigned char *key, const unsigned char *iv);
""")

def _resolve_binary_path() -> str:
    """
    Locates the platform-specific pre-compiled native machine library asset.
    Dynamically tests CPU feature level capability to load AVX2 or generic targets.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    binaries_dir = os.path.abspath(os.path.join(base_dir, "..", "Binaries"))
    
    if sys.platform.startswith("win"):
        path_avx2 = os.path.join(binaries_dir, "libnullfox_windows_avx2.dll")
        path_generic = os.path.join(binaries_dir, "libnullfox_windows_generic.dll")
        
        if os.path.exists(path_avx2):
            try:
                test_load = ffi.dlopen(path_avx2)
                del test_load
                return path_avx2
            except Exception:
                pass
                
        if os.path.exists(path_generic):
            return path_generic
        raise FileNotFoundError("Critical System Fault: No compatible Windows native library asset found.")
        
    elif sys.platform.startswith("linux"):
        # Detect if we are executing inside an Android environment
        if "ANDROID_DATA" in os.environ:
            # Check the system architecture profile to load the perfect match
            import platform
            arch = platform.machine().lower()
            
            if "x86_64" in arch or "amd64" in arch:
                return os.path.join(binaries_dir, "libnullfox_android_x86_64.so")
            else:
                # Default fallback for real physical ARM64 devices
                return os.path.join(binaries_dir, "libnullfox_android.so")
            
        path_avx2 = os.path.join(binaries_dir, "libnullfox_linux_avx2.so")
        path_generic = os.path.join(binaries_dir, "libnullfox_linux_generic.so")
        
        if os.path.exists(path_avx2):
            try:
                test_load = ffi.dlopen(path_avx2)
                del test_load
                return path_avx2
            except Exception:
                pass
                
        if os.path.exists(path_generic):
            return path_generic
        raise FileNotFoundError("Critical System Fault: No compatible Linux native library asset found.")
        
    else:
        raise OSError(f"Unsupported operating system runtime target environment: {sys.platform}")
    
_lib_path = _resolve_binary_path()
if not os.path.exists(_lib_path):
    raise FileNotFoundError(f"Critical System Fault: Native binary asset missing at target path: '{_lib_path}'")

_native_lib = ffi.dlopen(_lib_path)


def generate_key() -> bytes:
    """
    Generates a standalone secure 32-byte (256-bit) AES key
    using cryptographically secure random token bytes.
    """
    return secrets.token_bytes(32)


def generate_iv() -> bytes:
    """
    Generates a standalone random 16-byte (128-bit) Initialization Vector (IV).
    Essential for unique cipher block layouts across individual encryption sessions.
    """
    return secrets.token_bytes(16)


def generate_key_pair() -> tuple:
    """
    Convenience function that generates and returns a matching secure
    Key and IV pair simultaneously.
    
    Returns:
        tuple: (key_bytes, iv_bytes)
    """
    return secrets.token_bytes(32), secrets.token_bytes(16)


def aes_encrypt_py(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    """
    Hardened Python wrapper for native block-level symmetric encryption.
    Strictly requires pre-allocated key and initialization vector parameters.
    """
    # Reject execution if parameters are completely omitted
    if key is None or iv is None:
        raise ValueError("Cryptographic Failure: Both 'key' and 'iv' parameters must be explicitly provided.")

    # Prevent buffer allocation anomalies with empty datasets
    if not plaintext or len(plaintext) == 0:
        raise ValueError("Cryptographic Failure: Cannot encrypt an empty or zero-byte payload.")
        
    # Strict key and initialization vector sizing validations
    if len(key) != 32:
        raise ValueError("Cryptographic Failure: AES-256 key constraint requires exactly 32 bytes.")
    if len(iv) != 16:
        raise ValueError("Cryptographic Failure: Initialization vector constraint requires exactly 16 bytes.")
        
    plaintext_len = len(plaintext)
    
    # Calculate maximum possible padded size to ensure sufficient buffer size
    max_ciphertext_len = plaintext_len + (16 - (plaintext_len % 16))
    ciphertext_buffer = ffi.new("unsigned char[]", max_ciphertext_len)
    
    # Invoke the optimized native C routine
    actual_cipher_len = _native_lib.nullfox_aes_encrypt(plaintext, plaintext_len, ciphertext_buffer, key, iv)
    if actual_cipher_len < 0:
        raise RuntimeError(f"Native Engine Execution Failure: C routine failed with code {actual_cipher_len}")
        
    # Explicitly cast unpacked memory arrays directly into clean Python bytes objects
    return bytes(ffi.unpack(ciphertext_buffer, actual_cipher_len))


def aes_decrypt_py(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    """
    Python wrapper for native block-level symmetric decryption.
    Strictly requires matching key and initialization vector components.
    """
    if key is None or iv is None:
        raise ValueError("Cryptographic Failure: Both 'key' and 'iv' parameters must be explicitly provided.")

    if len(key) != 32 or len(iv) != 16:
        raise ValueError("Cryptographic Failure: Key must be exactly 32 bytes and IV must be exactly 16 bytes.")
        
    ciphertext_len = len(ciphertext)
    plaintext_buffer = ffi.new("unsigned char[]", ciphertext_len)
    
    # Invoke the native C decryption subroutine
    actual_plain_len = _native_lib.nullfox_aes_decrypt(ciphertext, ciphertext_len, plaintext_buffer, key, iv)
    if actual_plain_len < 0:
        raise RuntimeError(f"Native Engine Execution Failure: C routine failed with code {actual_plain_len}")
        
    # Explicitly unpack data into standard Python bytes objects
    return bytes(ffi.unpack(plaintext_buffer, actual_plain_len))


def encrypt_file(input_path: str, output_path: str, key: bytes, iv: bytes) -> int:
    """Python wrapper triggering native direct file encryption."""
    if key is None or iv is None:
        raise ValueError("Cryptographic Failure: Both 'key' and 'iv' parameters must be explicitly provided.")
    if len(key) != 32 or len(iv) != 16:
        raise ValueError("Cryptographic Failure: Key must be 32 bytes and IV must be 16 bytes.")

    c_input = ffi.new("char[]", input_path.encode('utf-8'))
    c_output = ffi.new("char[]", output_path.encode('utf-8'))
    return _native_lib.nullfox_file_encrypt(c_input, c_output, key, iv)


def decrypt_file(input_path: str, output_path: str, key: bytes, iv: bytes) -> int:
    """Python wrapper triggering native direct file decryption."""
    if key is None or iv is None:
        raise ValueError("Cryptographic Failure: Both 'key' and 'iv' parameters must be explicitly provided.")
    if len(key) != 32 or len(iv) != 16:
        raise ValueError("Cryptographic Failure: Key must be 32 bytes and IV must be 16 bytes.")

    c_input = ffi.new("char[]", input_path.encode('utf-8'))
    c_output = ffi.new("char[]", output_path.encode('utf-8'))
    return _native_lib.nullfox_file_decrypt(c_input, c_output, key, iv)