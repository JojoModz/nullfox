#include <stdio.h>
#include "aes_engine.h"

int nullfox_aes_encrypt(const unsigned char *plaintext, int plaintext_len, unsigned char *ciphertext, const unsigned char *key, const unsigned char *iv) {
    if(plaintext == NULL || plaintext_len <= 0 || key == NULL || iv == NULL) {
        printf("ERROR: Please ensure you have entered all the required fields! If you have filled all fields, please submit your error and code to me.\n");
        return -1;
    }

//  int len = 0;
//  int ciphertext_len = 0;
    int body_bytes = 0;
    int padding_bytes = 0;
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();

    if(ctx == NULL) {
        printf("ERROR: FATAL ERROR: Failed to encrypt! Check your RAM usage!\n");
        return -1;
    }

    if(EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        printf("ERROR: FATAL ERROR: Initialization of engine failed!\n");
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

    if(EVP_EncryptUpdate(ctx, ciphertext, &body_bytes, plaintext, plaintext_len) != 1) {
        printf("ERROR: FATAL ERROR: Encryption failed!\n");
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

//  ciphertext_len = len;

    if(EVP_EncryptFinal_ex(ctx, ciphertext + body_bytes, &padding_bytes) != 1) {
        printf("ERROR: FATAL ERROR: Please ensure your key and IV match the expected size constraints!\n");
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

    // ciphertext_len += len;
    body_bytes += padding_bytes;
    EVP_CIPHER_CTX_free(ctx);
    return body_bytes;
}

int nullfox_aes_decrypt(const unsigned char *ciphertext, int ciphertext_len, unsigned char *plaintext, const unsigned char *key, const unsigned char *iv) {
    if(ciphertext == NULL || ciphertext_len <= 0 || key == NULL || iv == NULL) {
        printf("ERROR: Please ensure you have entered all the required fields! If you have filled all fields, please submit your error and code to me.\n");
        return -1;
    }

//  int len = 0;
//  int plaintext_len = 0;
    int recovered_bytes = 0;
    int stripped_bytes = 0;
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();

    if(ctx == NULL) {
        printf("ERROR: FATAL ERROR: Failed to decrypt! Check your RAM usage!\n");
        return -1;
    }

    if(EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        printf("ERROR: FATAL ERROR: Initialization of engine failed!\n");
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

    if(EVP_DecryptUpdate(ctx, plaintext, &recovered_bytes, ciphertext, ciphertext_len) != 1) {
        printf("ERROR: FATAL ERROR: Decryption failed!\n");
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

//  plaintext_len = len;

    if(EVP_DecryptFinal_ex(ctx, plaintext + recovered_bytes, &stripped_bytes) != 1) {
        printf("ERROR: Please ensure you have entered the same key and IV used for encryption! Otherwise please ensure your key and IV match the expected size constraints!\n");
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

//  plaintext_len += len;
    recovered_bytes += stripped_bytes;
    EVP_CIPHER_CTX_free(ctx);
    return recovered_bytes;
}

int nullfox_file_encrypt(const char *input_path, const char *output_path, const unsigned char *key, const unsigned char *iv) {
    FILE *in = NULL;
    FILE *out = NULL;
    unsigned char buffer[65536];
    unsigned char out_buff[66560];
//  int len = 0;
    int chunk_out_len = 0;
    int final_block_len = 0;

    if(input_path == NULL || output_path == NULL || key == NULL || iv == NULL) {
        printf("ERROR: Please check that all required fields are entered and try again!\n");
        return -1;
    }

    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();

    if(ctx == NULL) {
        printf("ERROR: FATAL ERROR: Failed to encrypt file! Check your RAM usage!\n");
        return -1;
    }

    in = fopen(input_path, "rb");
    out = fopen(output_path, "wb");
/*  
    if(in == NULL || out == NULL) {
        printf("ERROR: FATAL ERROR: No input files!\n");
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }
*/

    if(in == NULL) {
        printf("ERROR: FATAL ERROR: No input files!\n");
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

    if(out == NULL) {
        printf("ERROR: FATAL ERROR: Cannot load output path!\n");
        fclose(in);
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

    if(EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        printf("ERROR: FATAL ERROR: Initalization of engine failed!\n");
        fclose(in);
        fclose(out);
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

    int read_len = 0;

    while((read_len = fread(buffer, 1, 65536, in)) > 0) {
        if(EVP_EncryptUpdate(ctx, out_buff, &chunk_out_len, buffer, read_len) != 1) {
            printf("ERROR: Encryption failed!\n");
            fclose(in);
            fclose(out);
            EVP_CIPHER_CTX_free(ctx);
            return -1;
        }

        fwrite(out_buff, 1, chunk_out_len, out);
    }

    if(EVP_EncryptFinal_ex(ctx, out_buff, &final_block_len) != 1) {
        printf("ERROR: Please ensure your key and IV are multiples of 16!\n");
        fclose(in);
        fclose(out);
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

    fwrite(out_buff, 1, final_block_len, out);

    fclose(in);
    fclose(out);
    EVP_CIPHER_CTX_free(ctx);
    return 0;
}

int nullfox_file_decrypt(const char *input_path, const char *output_path, const unsigned char *key, const unsigned char *iv) {
    FILE *in = NULL;
    FILE *out = NULL;
    unsigned char buffer[65536];
    unsigned char out_buff[66560];
//  int len = 0;
    int chunk_out_len = 0;
    int final_block_len = 0;

    if(input_path == NULL || output_path == NULL || key == NULL || iv == NULL) {
      printf("ERROR: Please check that all required fields are entered and try again!\n");
      return -1;
    }

    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();

    if(ctx == NULL) {
        printf("ERROR: FATAL ERROR: Failed to decrypt file! Check your RAM usage!\n");
        return -1;
    }

    in = fopen(input_path, "rb");
    out = fopen(output_path, "wb");

/*
    if(in == NULL || out == NULL) {
        printf("ERROR: FATAL ERROR: No input files!\n");
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }
*/

    if(in == NULL) {
        printf("ERROR: FATAL ERROR: No input files!\n");
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

    if(out == NULL) {
        printf("ERROR: FATAL ERROR: Cannot load output path!\n");
        fclose(in);
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

    if(EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv) != 1) {
        printf("ERROR: FATAL ERROR: Initalization of engine failed!\n");
        fclose(in);
        fclose(out);
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

    int read_len = 0;
    
    while((read_len = fread(buffer, 1, 65536, in)) > 0) {
        if(EVP_DecryptUpdate(ctx, out_buff, &chunk_out_len, buffer, read_len) != 1) {
            printf("ERROR: Decryption failed!\n");
            fclose(in);
            fclose(out);
            EVP_CIPHER_CTX_free(ctx);
            return -1;
        }
        fwrite(out_buff, 1, chunk_out_len, out);
    }

    if(EVP_DecryptFinal_ex(ctx, out_buff, &final_block_len) != 1) {
        printf("ERROR: Please ensure your key and IV are the same used for encryption!\n");
        fclose(in);
        fclose(out);
        EVP_CIPHER_CTX_free(ctx);
        return -1;
    }

    fwrite(out_buff, 1, final_block_len, out);

    fclose(in);
    fclose(out);
    EVP_CIPHER_CTX_free(ctx);
    return 0;
}