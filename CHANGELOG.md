# Changelog - NullFox Encryption Suite

All notable changes to this project will be documented in this file. The format is based on Keep a Changelog, and this project adheres to Semantic Versioning.

## [0.6.0] - 2026-05-21

### Added
- Native C engine cross-platform library support targeting Windows (`.dll`), Linux (`.so`), and Android (`.so`) platforms.
- Native AES-256 (Cipher Block Chaining) block cipher encryption and decryption algorithms.
- Native SHA-256 cryptographic hashing pipeline bindings for high-performance execution.
- Deterministic Key Derivation Function (KDF) stretching human-readable passphrases into 32-byte keys and 16-byte initialization vectors automatically.
- Universal file system streaming architecture capable of handling arbitrary binary payloads, asset blocks, and scripts.

### Changed
- Reconfigured package assembly pipeline to include multi-platform binary assets within standard distribution wheels.
- Upgraded configuration tracking schema to conform to standard unified metadata conventions.

### Removed
- Deprecated dynamic memory runtime loader systems to eliminate host execution overhead and stability conflicts.
- Removed plain-text Base64 obfuscation routines in favor of standardized raw binary array operations.

## [0.5.0] - 2026-04-04

### Added
- Runtime validation helper script boundaries.
- Auxiliary runtime formatting configuration modules.
- Environment pipeline support parameters.

### Fixed
- Decoding crashes occurring during structured text parsing operations.
- Intermittent logic execution faults inside background processing hooks.

### Improved
- General code structure organization and file tracking cleanup.

## [0.4.0] - 2025-12-07

### Fixed
- Internal namespace import resolution block mismatch during module linking phase.

### Changed
- Project configuration metadata alignment to support standard software deployment specifications.

## [0.3.0] - 2025-12-06

### Added
- Foundational file transformation operations utilizing combined basic transformation matrices.
- Early stage isolated interpretation sandbox module for execution verification routines.