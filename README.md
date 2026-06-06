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
```

## Binary Security Verification

To ensure the integrity of the pre-compiled native engines without requiring public C source files, you can verify the exact cryptographic signatures matching the distribution binaries against their official public VirusTotal scan results:

* **libnullfox_windows.dll (SHA-256):** `3AE3778EFABFBA85F685E0BFF245F1CDF85EC1339C3F1DD2747FAE002C88B47C`
  * [VirusTotal Hash Analysis Report](https://www.virustotal.com/gui/file/3ae3778efabfba85f685e0bff245f1cdf85ec1339c3f1dd2747fae002c88b47c)

* **libnullfox_linux.so (SHA-256):** `2135B735B0DA807A8702CFD902CC853635713FC48AD14681BB60B6DBECE8CAFD`
  * [VirusTotal Hash Analysis Report](https://www.virustotal.com/gui/file/2135b735b0da807a8702cfd902cc853635713fc48ad14681bb60b6dbece8cafd)

* **libnullfox_android.so (SHA-256):** `D070AE643720C4AEB186658E22BB551F888FFFB72BE52B1287AE30567CD4834E`
  * [VirusTotal Hash Analysis Report](https://www.virustotal.com/gui/file/d070ae643720c4aeb186658e22bb551f888fffb72be52b1287ae30567cd4834e)
