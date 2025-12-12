#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def encrypt_transposition(text, key):
    text = text.replace(" ", "")
    num_cols = len(key)
    num_rows = -(-len(text) // num_cols)
    text += " " * (num_rows * num_cols - len(text))
    
    grid = []
    for i in range(num_rows):
        row = list(text[i * num_cols:(i + 1) * num_cols])
        grid.append(row)
    
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    
    cipher_text = ""
    for col in key_order:
        for row in grid:
            cipher_text += row[col]
    
    return cipher_text

def decrypt_transposition(cipher_text, key):
    num_cols = len(key)
    num_rows = len(cipher_text) // num_cols
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    grid = [[''] * num_cols for _ in range(num_rows)]
    
    index = 0
    for col in key_order:
        for row in range(num_rows):
            grid[row][col] = cipher_text[index]
            index += 1
    
    plain_text = ""
    for row in grid:
        plain_text += "".join(row)
    
    return plain_text.rstrip()

original_text = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
key = "КЛЮЧ"

print("=" * 70)
print("ШИФР ПЕРЕСТАНОВКИ (COLUMNAR TRANSPOSITION CIPHER)")
print("=" * 70)
print()
print(f"Исходный текст:")
print(f"  {original_text}")
print()
print(f"Ключ шифрования: {key}")
print()

encrypted = encrypt_transposition(original_text, key)
print(f"Зашифрованный текст:")
print(f"  {encrypted}")
print()

text_no_spaces = original_text.replace(" ", "")
print(f"Текст без пробелов: {text_no_spaces}")
print(f"Длина: {len(text_no_spaces)} символов")
print()

decrypted = decrypt_transposition(encrypted, key)
print(f"Расшифрованный текст:")
print(f"  {decrypted}")
print()
print("=" * 70)
