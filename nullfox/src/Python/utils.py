"""
NullFox Encrypter Utility Subroutines
Provides internal helper metrics and foundational symmetric operations 
for data stream transformations.
"""

def xor_encrypt(data: bytes, key: str) -> bytes:
    """
    Executes a symmetric bitwise XOR operation against a target byte stream
    using a repeating key sequence.

    Args:
        data (bytes): The raw incoming byte payload to be transformed.
        key (str): The symmetric string key used to derive the XOR masking sequence.

    Returns:
        bytes: The resulting transformed ciphertext or plaintext byte sequence.
    """
    if not key:
        raise ValueError("Utility execution failure: Symmetric transformation key cannot be empty.")

    key_bytes = key.encode('utf-8')
    key_length = len(key_bytes)
    
    # Process sequential streaming transformations via cyclic array slicing
    return bytes([b ^ key_bytes[i % key_length] for i, b in enumerate(data)])