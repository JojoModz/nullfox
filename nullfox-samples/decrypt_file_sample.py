"""
NullFox Cryptographic Suite - High-Level File Decryption Sample
Demonstrates the secure recovery of disk containers using pre-existing hex-encoded 
tokens and the high-level hybrid processing API.
"""

import os
import nullfox.src.Python.engine_backend as fox

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    encrypted_container = os.path.join(base_dir, "secure_container.enc")
    recovered_file = os.path.join(base_dir, "restored_output.txt")
    token_cache = os.path.join(base_dir, ".keys")

    print("--- NullFox High-Level File Decryption Process ---")

    if not os.path.exists(encrypted_container) or not os.path.exists(token_cache):
        print("\n[X] Workspace Fault: Target container or token cache file missing.")
        return

    try:
        # Load the auto-generated keys from the cache file
        with open(token_cache, "r", encoding="utf-8") as f:
            hex_key = f.readline().strip()
            hex_iv = f.readline().strip()

        print(f"[...] Loaded keys from cache file successfully.")
        print(f"[...] Streaming payload out of container: '{encrypted_container}'")

        # Execute native file decryption
        success = fox.decrypt_file(
            input_path=encrypted_container,
            output_path=recovered_file,
            key=hex_key,
            iv=hex_iv
        )

        if success:
            print("\n[✓] Decryption Successful!")
            print("----------------------------------------------------------------")
            print(f"Recovered asset written to: '{recovered_file}'")
            print("----------------------------------------------------------------")
            
            with open(recovered_file, "r", encoding="utf-8") as f:
                print(f"Data Payload Preview: \"{f.read()}\"")
            print("----------------------------------------------------------------")

    except Exception as e:
        print(f"\n[X] Critical Engine Fault Occurred During File Decryption: {e}")

if __name__ == "__main__":
    main()