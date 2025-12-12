#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def encrypt_transposition(text, key):
    """Encrypts text using columnar transposition cipher"""
    text_no_spaces = text.replace(" ", "")
    rows = (len(text_no_spaces) + key - 1) // key
    
    matrix = []
    index = 0
    
    for i in range(rows):
        row = []
        for j in range(key):
            if index < len(text_no_spaces):
                row.append(text_no_spaces[index])
                index += 1
            else:
                row.append('_')
        matrix.append(row)
    
    encrypted = ""
    for col in range(key):
        for row in range(rows):
            encrypted += matrix[row][col]
    
    return encrypted


def decrypt_transposition(encrypted_text, key):
    """Decrypts text using columnar transposition cipher"""
    rows = (len(encrypted_text) + key - 1) // key
    
    matrix = [[''] * key for _ in range(rows)]
    
    index = 0
    for col in range(key):
        for row in range(rows):
            if index < len(encrypted_text):
                matrix[row][col] = encrypted_text[index]
                index += 1
    
    decrypted = ""
    for row in matrix:
        decrypted += ''.join(row)
    
    decrypted = decrypted.replace('_', '')
    
    return decrypted


def display_matrix(text, key):
    """Display encryption matrix for visualization"""
    text_no_spaces = text.replace(" ", "")
    rows = (len(text_no_spaces) + key - 1) // key
    
    matrix = []
    index = 0
    
    for i in range(rows):
        row = []
        for j in range(key):
            if index < len(text_no_spaces):
                row.append(text_no_spaces[index])
                index += 1
            else:
                row.append('_')
        matrix.append(row)
    
    print("\nEncryption Matrix:")
    print("=" * (key * 3))
    for row in matrix:
        print(' '.join(row))
    print("=" * (key * 3))


if __name__ == "__main__":
    original_text = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
    
    print("=" * 70)
    print("COLUMNAR TRANSPOSITION CIPHER ENCRYPTION")
    print("=" * 70)
    
    print(f"\nOriginal text:\n{original_text}")
    print(f"\nText length: {len(original_text)} characters")
    print(f"Length without spaces: {len(original_text.replace(' ', ''))} characters")
    
    key = 7
    
    print(f"\nEncryption key: {key} columns")
    
    encrypted = encrypt_transposition(original_text, key)
    
    display_matrix(original_text, key)
    
    print(f"\nEncrypted text:")
    print(encrypted)
    
    print(f"\nEncrypted text length: {len(encrypted)} characters")
    
    print("\n" + "=" * 70)
    print("DECRYPTION VERIFICATION")
    print("=" * 70)
    
    decrypted = decrypt_transposition(encrypted, key)
    print(f"\nDecrypted text:")
    print(decrypted)
    
    if decrypted == original_text.replace(" ", ""):
        print("\nEncryption and decryption successful!")
    else:
        print("\nError in encryption/decryption process")
    
    print("\n" + "=" * 70)
    print("ADDITIONAL VARIANTS WITH DIFFERENT KEYS")
    print("=" * 70)
    
    for test_key in [5, 8, 10]:
        encrypted_test = encrypt_transposition(original_text, test_key)
        print(f"\nKey {test_key}: {encrypted_test}")
