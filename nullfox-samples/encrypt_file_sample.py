"""
NullFox Cryptographic Suite - High-Level File Encryption Sample
Demonstrates the secure encryption of disk containers utilizing the optimized
native 64KB streaming engine and automatic credential tracking tokens.
"""

import os
import nullfox.src.Python.engine_backend as fox

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source_file = os.path.join(base_dir, "sample-file.txt")
    encrypted_container = os.path.join(base_dir, "secure_container.enc")
    token_cache = os.path.join(base_dir, ".keys")

    print("--- NullFox High-Level File Encryption Process ---")

    if not os.path.exists(source_file):
        with open(source_file, "w", encoding="utf-8") as f:
            f.write("This is highly sensitive corporate asset data routed through NullFox v0.7.0.")
        print(f"[✓] Generated dummy target file: '{source_file}'")

    try:
        print(f"[...] Initializing native streaming buffer for: '{source_file}'")
        
        # Execute file encryption
        key, iv = fox.encrypt_file(input_path=source_file, output_path=encrypted_container)

        # Cache the tokens automatically so you don't have to copy-paste them
        with open(token_cache, "w", encoding="utf-8") as f:
            f.write(f"{key.hex()}\n{iv.hex()}")

        print("[✓] Native Streaming Core: SUCCESS")
        print(f"    ↳ Encrypted container saved to: '{encrypted_container}'")
        print(f"    ↳ Security tokens auto-cached for test run.")

    except Exception as e:
        print(f"\n[X] Critical Engine Fault Occurred During File Encryption: {e}")

if __name__ == "__main__":
    main()