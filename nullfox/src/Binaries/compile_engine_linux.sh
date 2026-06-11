#!/bin/bash
# ====================================================================
# NullFox Native Engine Multi-Target Compilation Script for Linux
# Targets x86-64 Feature Levels for AVX2 Hardware Acceleration
# ====================================================================
# To unlock execution permission use: chmod +x compile_engine_linux.sh

echo "[Build System] Initializing native C engine Linux compilation matrix..."

# 1. Verify source file path security
if [ ! -f "../C/aes_engine.c" ]; then
    echo "[Build Error] Technical Fault: Source asset '../C/aes_engine.c' could not be resolved."
    exit 1
fi

# 2. Compile Feature Level 3 Binary (AVX2 Accelerated Layer)
echo "[Build System] Compiling Linux Feature Level 3 (AVX2 Accelerated) target..."
gcc -O3 -shared -fPIC -march=x86-64-v3 "../C/aes_engine.c" -o "libnullfox_linux_avx2.so" -lcrypto

if [ $? -ne 0 ]; then
    echo "[Build Error] Technical Fault: Linux Feature Level 3 compilation failed."
    exit 1
fi

# 3. Compile Feature Level 2 Binary (Generic Compatibility Fallback Layer)
echo "[Build System] Compiling Linux Feature Level 2 (Generic Fallback) target..."
gcc -O3 -shared -fPIC -march=x86-64-v2 "../C/aes_engine.c" -o "libnullfox_linux_generic.so" -lcrypto

if [ $? -ne 0 ]; then
    echo "[Build Error] Technical Fault: Linux Feature Level 2 compilation failed."
    exit 1
fi

echo "[Build System] Linux compilation matrix clear. Native library assets successfully deployed."
exit 0