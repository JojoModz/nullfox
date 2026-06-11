@echo off
rem ====================================================================
rem NullFox Native Engine Multi-Target Compilation Script for Windows
rem ====================================================================

echo [Build System] Init native C engine compilation matrix...

if not exist "..\C\aes_engine.c" (
    echo [Build Error] Technical Fault: Source asset '..\C\aes_engine.c' could not be resolved.
    exit /b 1
)

rem --------------------------------------------------------------------
rem NESTING DOLL SOLVED: Exact Windows OpenSSL 64-bit Directory Maps
rem --------------------------------------------------------------------
set WIN_OPENSSL_INC=D:\OpenSSL-Win64\include
set WIN_OPENSSL_LIB_FILE=D:\OpenSSL-Win64\lib\VC\x64\MD\libcrypto.lib

rem 2. Compile Feature Level 3 Binary (AVX2 Accelerated Layer)
echo [Build System] Compiling Feature Level 3 (AVX2 Accelerated) target...
gcc -O3 -shared -fPIC -march=x86-64-v3 -I"%WIN_OPENSSL_INC%" "..\C\aes_engine.c" "%WIN_OPENSSL_LIB_FILE%" -o "libnullfox_windows_avx2.dll"

if %errorlevel% neq 0 (
    echo [Build Error] Technical Fault: Feature Level 3 compilation failed.
    exit /b 1
)

rem 3. Compile Feature Level 2 Binary (Generic Compatibility Fallback Layer)
echo [Build System] Compiling Feature Level 2 (Generic Fallback) target...
gcc -O3 -shared -fPIC -march=x86-64-v2 -I"%WIN_OPENSSL_INC%" "..\C\aes_engine.c" "%WIN_OPENSSL_LIB_FILE%" -o "libnullfox_windows_generic.dll"

if %errorlevel% neq 0 (
    echo [Build Error] Technical Fault: Feature Level 2 compilation failed.
    exit /b 1
)

echo [Build System] Windows compilation matrix clear. Native library assets successfully deployed.
exit /b 0