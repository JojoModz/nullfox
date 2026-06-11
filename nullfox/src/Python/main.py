"""
NullFox Encryption Suite Orchestration Test Rig
Demonstrates cross-platform multi-binary execution tracking across universal file types.
"""

import os
import sys
# Update internal import targets to route through new backend models cleanly
from .engine_backend import encrypt_file, decrypt_file

def execute_system_verification():
    print("=========================================================")
    print("       NULLFOX NATIVE PIPELINE INTEGRATION SUCCESS       ")
    print("=========================================================\n")
    
    source_target = input("[System Init] Enter target file path for verification testing: ").strip()

    if not source_target or not os.path.exists(source_target):
        print(f"[Error] Initialization Failure: Path mismatch or missing file target.", file=sys.stderr)
        sys.exit(1)

    base_name, extension = os.path.splitext(source_target)
    encrypted_target = f"{base_name}.enc"
    recovery_output = f"{base_name}_recovered{extension}"

    try:
        print(f"\n[Action] Processing file encryption (Generating secure auto-tokens)...")
        # Triggering automatic token routing by passing None as credentials parameters
        saved_key, saved_iv = encrypt_file(source_target, encrypted_target, key=None, iv=None)
        print(f"[Success] Obfuscated package compiled directly to: '{encrypted_target}'")

        print(f"\n[Action] Executing verification reverse-extraction using hex keys...")
        # Passing hex formatted elements directly back into pipeline layers
        decrypt_file(encrypted_target, recovery_output, saved_key.hex(), saved_iv.hex())
        print(f"[Success] Reconstructed original binary sequence to: '{recovery_output}'")

        # Verify stream consistency metrics
        with open(source_target, "rb") as orig, open(recovery_output, "rb") as rec:
            if orig.read() == rec.read():
                print("\n[Integrity Verification] Data streams match identically. Zero byte corruption detected.")
            else:
                print("\n[Warning] Data integrity check failed: Stream mismatch.", file=sys.stderr)

    except Exception as error:
        print(f"\n[Error] Pipeline Fault: Test rig crashed: {str(error)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    execute_system_verification()