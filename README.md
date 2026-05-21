# NullFox Encryption Suite

An enterprise-grade, high-performance cross-platform universal file encryption toolkit utilizing optimized native AES-256 (Cipher Block Chaining) and SHA-256 machine engines.

## Features

* **Multi-Platform Native Acceleration**: Built-in architecture tracking across Microsoft Windows (`.dll`), Linux Desktop (`.so`), and Google Android (`.so`) runtime target boundaries.
* **Cryptographic Rigor**: High-speed symmetric file protection using AES-256-CBC block ciphers powered by direct native C Foreign Function Interface (CFFI) memory binds.
* **Deterministic Key Derivation**: Transparent variable-length master password stretching via custom SHA-256 hashing routines, completely removing the requirement for manual initialization vector inputs.
* **Universal Stream Support**: Pure binary-safe sequential tracking capable of processing any digital asset, including script source files, binary application components, imagery, and database backups.
* **Zero Host Pollution**: Clean, lightweight integration boundary with zero loose environmental footprint requirements or external library runtime runtime dependencies.

## Architecture Map

The NullFox layout automatically distributes and binds pre-compiled native binaries matching the current execution environment profile:

* `libnullfox_windows.dll` — Native machine target module for Windows Desktop x86_64 architectures.
* `libnullfox_linux.so` — Native machine target module for Linux Desktop x86_64 environments.
* `libnullfox_android.so` — Native machine target module for Android Mobile ARM64 architectures.

## Installation

Install the library along with its structural C-bridge prerequisites directly via your local directory toolchain:

```bash
pip install .