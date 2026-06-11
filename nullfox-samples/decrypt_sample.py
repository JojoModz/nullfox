"""
NullFox Cryptographic Suite - High-Level Decryption Sample
Demonstrates the secure recovery of encrypted byte data using existing hex-encoded tokens
and the high-level hybrid processing API.
"""

import nullfox.src.Python.engine_backend as fox

def main():
    # 1. Inputs: Replace these placeholders with the hex outputs from your encryption run.
    hex_key = "94c00963023d4c564fd2008ccb71d03f1df8b49747fb1abfb55361b5e3ee3dde"
    hex_iv = "163f9eaf6a97fab0930cfe68087b7eba"
    hex_ciphertext = "6bea784f05920e5ef9390dcd5aa31527f28f4ef06da4b9f662568978f940057aed4a71fd94594b57cc2bc0e0046ec42f220e6fc5d8e07806cf5887eee398ac6d"

    print("--- NullFox High-Level Decryption Process ---")

    try:
        # 2. Execute hybrid memory decryption loop
        # The backend automatically handles hex-to-bytes translation internally!
        decrypted_payload = fox.decrypt_string(
            ciphertext=bytes.fromhex(hex_ciphertext), 
            key=hex_key, 
            iv=hex_iv
        )

        # 3. Display the recovered original data
        print("\n[✓] Decryption Successful!")
        print("----------------------------------------------------------------")
        print(f"Recovered Plaintext: {decrypted_payload.decode('utf-8')}")
        print("----------------------------------------------------------------")

    except ValueError:
        print("\n[X] Format Error: Invalid hexadecimal string configuration provided.")
    except Exception as e:
        print(f"\n[X] Critical Fault Occurred During Decryption: {e}")

if __name__ == "__main__":
    main()