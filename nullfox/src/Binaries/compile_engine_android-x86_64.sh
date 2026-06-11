#!/bin/bash
# ==============================================================================
# NullFox Security Core - Native Engine Cross-Compilation Framework
# Module:      Android Emulator Target (x86_64)
# Description: Automated LLVM-Clang Toolchain Discovery and Cross-Compilation
#              Pipeline utilizing Static OpenSSL Layer Injection for Intel/AMD Emulators.
# Platform:    Cross-Platform Host Support (Windows Git-Bash / Native Linux / WSL)
# ==============================================================================

set -e # Terminate script immediately if any individual command drops a failure status

echo "=============================================================================="
echo "[NullFox Build Core] Initializing Android x86_64 Native Engine Compilation..."
echo "=============================================================================="

#-------------------------------------------------------------------------------
# 1. PATH MATRIX DEFINITIONS
#-------------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DEPS_DIR="$(cd "${SCRIPT_DIR}/../../deps/openssl-android" && pwd)"

# Resolve relative target artifacts based on verified repository layout structure
OPENSSL_STATIC_A="${ROOT_DEPS_DIR}/3.0/openssl-3.0.20/android-x86_64/libcrypto.a"
OPENSSL_INCLUDE="${ROOT_DEPS_DIR}/3.0/openssl-3.0.20/android-x86_64/include"
SRC_ENGINE_C="$(cd "${SCRIPT_DIR}/../C" && pwd)/aes_engine.c"
OUTPUT_BINARY="${SCRIPT_DIR}/libnullfox_android_x86_64.so"

#-------------------------------------------------------------------------------
# 2. DYNAMIC NDK TOOLCHAIN DISCOVERY ENGINE
#-------------------------------------------------------------------------------
echo "[Build System] Launching dynamic Android NDK asset search matrix..."
NDK_FOUND_PATH=""

POSSIBLE_NDK_ROOTS=(
    "/d/Android_SDK/ndk"
    "/mnt/d/Android_SDK/ndk"
    "D:/Android_SDK/ndk"
    "$HOME/AppData/Local/Android/Sdk/ndk"
    "/c/Users/$USER/AppData/Local/Android/Sdk/ndk"
    "/mnt/c/Users/$USER/AppData/Local/Android/Sdk/ndk"
    "/usr/local/lib/android/sdk/ndk"
)

for root in "${POSSIBLE_NDK_ROOTS[@]}"; do
    if [ -d "$root" ]; then
        HIGHEST_VERSION=$(ls -1 "$root" 2>/dev/null | sort -V | tail -n 1)
        if [ ! -z "$HIGHEST_VERSION" ]; then
            TARGET_BIN_DIR="$root/$HIGHEST_VERSION/toolchains/llvm/prebuilt/windows-x86_64/bin"
            if [ ! -d "$TARGET_BIN_DIR" ]; then
                TARGET_BIN_DIR="$root/$HIGHEST_VERSION/toolchains/llvm/prebuilt/linux-x86_64/bin"
            fi

            if [ -d "$TARGET_BIN_DIR" ]; then
                NDK_FOUND_PATH="$TARGET_BIN_DIR"
                echo "[Build System] Verified NDK Target Located: $root/$HIGHEST_VERSION"
                break
            fi
        fi
    fi
done

if [ -z "$NDK_FOUND_PATH" ] && [ ! -z "$NDK_TOOLCHAIN_PATH" ]; then
    NDK_FOUND_PATH="$NDK_TOOLCHAIN_PATH"
fi

if [ -z "$NDK_FOUND_PATH" ]; then
    echo " "
    echo "[CRITICAL FAULT] Android NDK compiler toolchain could not be auto-discovered."
    echo "=============================================================================="
    exit 1
fi

#-------------------------------------------------------------------------------
# 3. COMPILER EXECUTABLE RESOLUTION
#-------------------------------------------------------------------------------
COMPILER_EXE="${NDK_FOUND_PATH}/x86_64-linux-android30-clang.exe"
if [ ! -f "$COMPILER_EXE" ]; then
    COMPILER_EXE="${NDK_FOUND_PATH}/x86_64-linux-android30-clang"
fi

#-------------------------------------------------------------------------------
# 4. WSL DIRECTORY PATH CONVERSION TRANSLATION FOR WINDOWS CLANG
#-------------------------------------------------------------------------------
# Dynamically converts our auto-discovered Linux mount points to standard Windows styles
WIN_SRC_C=$(wslpath -w "$SRC_ENGINE_C")
WIN_STATIC_A=$(wslpath -w "$OPENSSL_STATIC_A")
WIN_INCLUDE=$(wslpath -w "$OPENSSL_INCLUDE")
WIN_OUTPUT=$(wslpath -w "$OUTPUT_BINARY")

#-------------------------------------------------------------------------------
# 5. PRE-FLIGHT INTEGRITY & SYSTEM DIAGNOSTICS
#-------------------------------------------------------------------------------
echo " "
echo "--- Build Target Diagnostics ---"
echo "  [+] Source Core Location:   ${SRC_ENGINE_C}"
echo "  [+] OpenSSL Headers Path:   ${OPENSSL_INCLUDE}"
echo "  [+] Static Library Object:  ${OPENSSL_STATIC_A}"
echo "  [+] Selected Compiler Core: ${COMPILER_EXE}"
echo "--------------------------------"
echo " "

if [ ! -f "$SRC_ENGINE_C" ]; then
    echo "[Build Error] Technical Fault: Native source code compilation unit unresolved."
    exit 1
fi

if [ ! -f "$OPENSSL_STATIC_A" ]; then
    echo "[Build Error] Dependency Fault: Required static object 'libcrypto.a' missing from target subsystem."
    exit 1
fi

#-------------------------------------------------------------------------------
# 6. EXECUTE PIPELINE COMPILATION
#-------------------------------------------------------------------------------
echo "[Build System] Invoking Android x86_64 Cross-Compiler Node..."

# Pass the translated Windows system strings directly into Clang execution
"$COMPILER_EXE" \
    -O3 -shared -fPIC \
    -I"$WIN_INCLUDE" \
    "$WIN_SRC_C" \
    "$WIN_STATIC_A" \
    -o "$WIN_OUTPUT"

if [ $? -eq 0 ]; then
    echo "=============================================================================="
    echo "[SUCCESS] Android x86_64 cross-compilation milestone clear."
    echo "[SUCCESS] Target Binary deployed to: ${OUTPUT_BINARY}"
    echo "=============================================================================="
    exit 0
else
    echo "=============================================================================="
    echo "[CRITICAL FAULT] Compilation hardware sub-process dropped non-zero exit status."
    echo "=============================================================================="
    exit 1
fi