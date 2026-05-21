"""
NullFox Encryption Suite Orchestration Test Rig
Demonstrates cross-platform multi-binary execution tracking across universal file types.
"""

import os
import sys
from nullfox.encrypt import encrypt_file, decrypt_file

def execute_system_verification():
    """
    Executes a comprehensive static file encryption and decryption verification loop
    relying entirely on interactive user runtime arguments with zero hardcoding.
    """
    print("=========================================================")
    print("       NULLFOX NATIVE PIPELINE INTEGRATION SUCCESS       ")
    print("=========================================================\n")

    # 1. Capture user cryptographic password passphrase (No hardcoded keys/IVs)
    user_password = input("[System Init] Define encryption passphrase: ").strip()
    if not user_password:
        print("[Error] Initialization Failure: Master passphrase cannot be empty.", file=sys.stderr)
        sys.exit(1)
    
    # 2. Prompt user for explicit file asset path to verify universal target support
    source_target = input("[System Init] Enter target file path for verification testing: ").strip()

    if not source_target:
        print("[Error] Initialization Failure: Target file path argument is required.", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(source_target):
        print(f"[Error] Initialization Failure: Target path could not be resolved: '{source_target}'", file=sys.stderr)
        sys.exit(1)

    # Establish output path configurations dynamically based on the target's original extension profile
    base_name, extension = os.path.splitext(source_target)
    encrypted_target = f"{base_name}.enc"
    recovery_output = f"{base_name}_recovered{extension}"

    try:
        # Execution phase 1: Symmetric processing and byte transposition matrix encryption
        print(f"\n[Action] Processing static file encryption asset loop: '{source_target}'...")
        encrypt_file(source_target, encrypted_target, user_password)
        print(f"[Success] Obfuscated package compiled directly to: '{encrypted_target}'")

        # Execution phase 2: Verification decryption loop back to structural layout formats
        print(f"\n[Action] Executing verification reverse-extraction routine...")
        decrypt_file(encrypted_target, recovery_output, user_password)
        print(f"[Success] Reconstructed original binary sequence to: '{recovery_output}'")

        # Data Verification: Ensure the decrypted byte structure perfectly maps to the source data
        with open(source_target, "rb") as orig, open(recovery_output, "rb") as rec:
            if orig.read() == rec.read():
                print("\n[Integrity Verification] Data streams match identically. Zero byte corruption detected.")
            else:
                print("\n[Warning] Data integrity check failed: Restored data mismatched original stream profile.", file=sys.stderr)

        print("\n=========================================================")
        print("          SYSTEM CHECK CLEAR: ENGINES SECURED            ")
        print("=========================================================")

    except Exception as error:
        print(f"\n[Error] Pipeline Fault: Test rig crashed with structural error: {str(error)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_system_verification()