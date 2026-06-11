"""
NullFox Cryptographic Suite - High-Level Encryption Sample
Demonstrates secure token auto-generation, string encryption, and hexadecimal exporting
using the enterprise-grade hybrid API architecture.
"""

import nullfox.src.Python.engine_backend as fox

def main():
    # 1. Define the sensitive data payload to be encrypted
    plaintext = b"Confidential financial records - 2026 Internal Audit."

    print("--- NullFox High-Level Encryption Process ---")
    print(f"[...] Input Plaintext: {plaintext.decode('utf-8')}")

    try:
        # 2. Execute hybrid memory encryption loop
        # Leaving key/iv empty triggers cryptographically secure auto-generation
        ciphertext, key, iv = fox.encrypt_string(plaintext)

        # 3. Display secure hexadecimal footprints for storage/transmission
        print("\n[✓] Encryption Successful!")
        print("----------------------------------------------------------------")
        print(f"Key (Hex):        {key.hex()}")
        print(f"IV (Hex):         {iv.hex()}")
        print(f"Ciphertext (Hex): {ciphertext.hex()}")
        print("----------------------------------------------------------------")
        print("CRITICAL: Securely archive the Key and IV footprint. Data recovery")
        print("is mathematically impossible without these exact tokens.")
        
    except Exception as e:
        print(f"\n[X] Critical Fault Occurred During Encryption: {e}")

if __name__ == "__main__":
    main()