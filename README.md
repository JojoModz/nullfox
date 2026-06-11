# NullFox Cryptographic Suite

[![PyPI Version](https://img.shields.io/pypi/v/nullfox?color=blue&style=flat-square)](https://pypi.org/project/nullfox/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Platform Support](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Android-brightgreen?style=flat-square)](#architecture-matrix)

A high-performance, cross-platform framework for universal data encryption utilizing hardware-optimized AES-256-CBC and SHA-256 engines.

## Overview

NullFox is an enterprise-grade cryptographic toolkit designed for secure data processing across multiple operating systems. By bridging a high-performance C engine with a hardened Python interface via CFFI (Foreign Function Interface), NullFox delivers military-grade symmetric encryption with minimal latency, single-line import routing, and zero external runtime dependencies.

## Key Features

* Single-Line Import Routing: Modernized top-level namespace integration allows calling tools via a unified interface (import nullfox) while completely preserving clean, isolated internal subfolder layouts.
* Strict Parameter Constraint Shield: Active verification layers immediately reject missing arguments (None) and enforce explicit credentials parsing before committing pointers to the native execution layer.
* Volatile Memory Sanitization: Built-in security hooks implement an automated try...finally memory dump wipe, leveraging CFFI buffers to zero-stamp (0x00) secret key arrays out of system RAM immediately post-use.
* Native Multi-Platform Acceleration: Native machine code execution support for Windows (.dll), Linux (.so), and Android (.so).
* Hardware Optimization: Dynamic runtime selection of AVX2, generic, ARM64, and x86_64 architecture cores to maximize CPU instruction-set throughput.
* Resource Efficient: Optimized 64KB streaming buffers designed for high-speed NVMe and mobile flash storage performance.

## Architecture Matrix

NullFox automatically resolves the optimal binary asset for the host environment at runtime:

| Operating System | Architecture | Binary Asset | Target Level |
| :--- | :--- | :--- | :--- |
| Windows | x86_64 | libnullfox_windows_avx2.dll | AVX2 Hardware Accel |
| Windows | x86_64 (Legacy) | libnullfox_windows_generic.dll | Standard x86-64 v2 |
| Linux / WSL | x86_64 | libnullfox_linux_avx2.so | AVX2 Hardware Accel |
| Linux / WSL | x86_64 (Generic) | libnullfox_linux_generic.so | POSIX Standard |
| Android | ARM64-v8a | libnullfox_android.so | AArch64 Production |
| Android Emulator| x86_64 | libnullfox_android_x86_64.so | NDK Virtual Target |

---

## Installation & Setup

### Standard Installation
The recommended method for standard deployments is via the Python package manager:
```bash
pip install nullfox
```
### Native Compilation from Source
For developers requiring custom builds, platform-specific compile scripts are located inside the nullfox/src/Binaries/ directory:

Windows (PowerShell / Batch):
```powershell
.\compile_engine_windows.bat
```
Linux / WSL (Bash):
```bash
./compile_engine_linux.sh
```

Android (NDK r30+):
```bash
./compile_engine_android.sh
```
---

## Implementation & Verification

The following production blueprints demonstrate the streamlined top-level API workflows for string operations and file streaming pipelines with strict parameter constraints:

### 1. In-Memory String Operations Workflow
```python
import nullfox

print("=== NULLFOX STRING CRYPTOGRAPHIC VERIFICATION ===")

try:
    # 1. Resource Initialization (Explicit Parameter Token Generation)
    key = nullfox.generate_key()  # 32-Byte Secure Token (AES-256)
    iv = nullfox.generate_iv()    # 16-Byte Initialization Vector (Block Aligned)

    print(f"[✓] Token Security Generation: SUCCESS")
    print(f"    ↳ Key (Hex): {key.hex()}")
    print(f"    ↳ IV (Hex):  {iv.hex()}\n")

    # 2. Data Payload Definition
    payload = b"Production Data Packet v0.7.0"
    print(f"[...] Passing payload into strict parameter backend...")

    # 3. Cryptographic Core Loops (Automatic Memory Sanitization Post-Execution)
    ciphertext, safe_key, safe_iv = nullfox.encrypt_string(payload, key, iv)
    decrypted = nullfox.decrypt_string(ciphertext, safe_key, safe_iv)

    # 4. Integrity Validation Check
    if decrypted == payload:
        print("\n[STATUS] Cryptographic Integrity: MATCHED & 100% STABLE")
    else:
        raise ValueError("Buffer unpacking payload mismatch detected.")

except Exception as e:
    print(f"\n[X] Cryptographic Fault Detected: {e}")
```
### 2. High-Speed File Streaming Workflow (64KB C-Buffer Routing)
```python
from nullfox import encrypt_file, decrypt_file, generate_key, generate_iv

try:
    # Generate explicit validation parameters
    key = generate_key()
    iv = generate_iv()

    # Native streaming execution via single-line front-gate routing
    encrypt_file("source_data.bin", "vault.enc", key, iv)
    decrypt_file("vault.enc", "recovered_data.bin", key, iv)
    print("[✓] Native Streaming Pipeline: SUCCESS")
    
except Exception as e:
    print(f"[X] Streaming Execution Error: {e}")
```
---

## Integrity Manifest

Verify the SHA-256 fingerprints of the distribution binaries against the official release signatures:

| Asset File | Target Architecture / SHA-256 Signature |
| :--- | :--- |
| libnullfox_windows_avx2.dll | [ d98e37c5baffe5f204718f3439966731a8e2c46d009e5a62e42b10f23ebf26bd ] |
| libnullfox_windows_generic.dll | [ 3e1b773db1d73192356f6f5110ddefb57357269926e86a2a161dfcd7195fa5e7 ] |
| libnullfox_linux_avx2.so | [ 1b549fe0b6b3627eb4c908d5e03fd8b48e6c1cf12cd6237eb846822c27e8487e ] |
| libnullfox_linux_generic.so | [ 1b549fe0b6b3627eb4c908d5e03fd8b48e6c1cf12cd6237eb846822c27e8487e ] |
| libnullfox_android.so | [ 64afab0de03e40d0a311c83dce2678f5ad5e19f3e308f7bad8b13e0de77f4360 ] |
| libnullfox_android_x86_64.so | [ 17ff73cf5fd550a47274f1467f563ffab709c1737e6966905da2bbdeaca73140 ] |

## License

NullFox is released under the open-source [MIT License](LICENCE).   