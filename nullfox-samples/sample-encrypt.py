"""
NullFox Encryption Suite - Production Reference Implementation
Demonstrates programmatic native C file encryption.
"""

import nullfox

def main():
    print("=========================================================")
    print("             NULLFOX NATIVE FILE ENCRYPTION              ")
    print("=========================================================\n")

    source_asset = "sample-file.txt"
    encrypted_output = "sample-file.enc"
    
    # 🔑 Define exact 32-byte encryption key and 16-byte IV constraints
    crypto_key = b"A_32_Byte_Secret_Key_NullFox_!!!"  # Exactly 32 bytes
    crypto_iv  = b"A_16_Byte_IV_!!!"                  # Exactly 16 bytes

    print(f"[Action] Requesting native encryption on: '{source_asset}'...")
    
    try:
        nullfox.encrypt_file(source_asset, encrypted_output, crypto_key, crypto_iv)
        print(f"[Success] Native binary encryption complete. Container deployed: '{encrypted_output}'")
    except Exception as error:
        print(f"[Error] Operation aborted: {str(error)}")

if __name__ == "__main__":
    main()