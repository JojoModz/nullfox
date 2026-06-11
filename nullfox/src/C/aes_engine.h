#ifndef NULLFOX_AES_H
#define NULLFOX_AES_H
#include <openssl/evp.h>

int nullfox_aes_encrypt(const unsigned char *plaintext, int plaintext_len, unsigned char *ciphertext, const unsigned char *key, const unsigned char *iv);
int nullfox_aes_decrypt(const unsigned char *ciphertext, int ciphertext_len, unsigned char *plaintext, const unsigned char *key, const unsigned char *iv);
int nullfox_file_encrypt(const char *input_path, const char *output_path, const unsigned char *key, const unsigned char *iv);
int nullfox_file_decrypt(const char *input_path, const char *output_path, const unsigned char *key, const unsigned char *iv);

#endif // NULLFOX_AES_H