"""
NullFox Encryption Suite - Production Reference Implementation
Demonstrates programmatic native C file decryption.
"""

import nullfox

def main():
    print("=========================================================")
    print("             NULLFOX NATIVE FILE DECRYPTION              ")
    print("=========================================================\n")

    encrypted_target = "sample-file.enc"
    recovered_output = "sample-file_recovered.txt"
    
    # 🔑 Must match the original parameters identically
    crypto_key = b"A_32_Byte_Secret_Key_NullFox_!!! "  # Exactly 32 bytes
    crypto_iv  = b"A_16_Byte_IV_!!! "                  # Exactly 16 bytes

    print(f"[Action] Requesting native reverse-extraction on: '{encrypted_target}'...")
    
    try:
        nullfox.decrypt_file(encrypted_target, recovered_output, crypto_key, crypto_iv)
        print(f"[Success] Native binary decryption complete. Asset restored: '{recovered_output}'")
    except Exception as error:
        print(f"[Error] Operation aborted: {str(error)}")

if __name__ == "__main__":
    main()