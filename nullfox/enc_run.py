"""
NullFox Encrypter Build Automation Utility
Provides a clean automation interface to statically encrypt source script assets 
for deployment distributions.
"""

import sys
import os
from nullfox.encrypt import encrypt_file

def run_build_compiler(source_path: str, output_path: str, secret_key: str, iv_bytes: bytes) -> None:
    """
    Statically compiles and encrypts a target source asset for secure production distribution.
    """
    print(f"[Build System] Initiating secure compilation layer for target: '{source_path}'")
    
    if not os.path.exists(source_path):
        print(f"[Build Error] Failed to resolve source script resource: {source_path}", file=sys.stderr)
        sys.exit(1)
        
    try:
        success = encrypt_file(source_path, output_path, secret_key, iv_bytes)
        if success:
            print(f"[Build Success] Production-ready cipher asset deployed directly to: '{output_path}'")
    except Exception as error:
        print(f"[Build Exception] Encryption pipeline failed with structural error: {str(error)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Example execution configuration block if run from the terminal directly
    # Adjust initialization parameters to match deployment criteria
    STATIC_KEY = "DefaultNullFoxSystemProductionKey"
    STATIC_IV = b"NullFoxEngine_IV!"  # Must remain exactly 16 bytes
    
    run_build_compiler("script.lua", "script.enc", STATIC_KEY, STATIC_IV)