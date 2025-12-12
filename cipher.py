#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def encrypt_transposition(plaintext, key):
    text = plaintext.replace(" ", "")
    num_cols = len(key)
    num_rows = len(text) // num_cols
    if len(text) % num_cols != 0:
        num_rows += 1
    
    padded_text = text.ljust(num_rows * num_cols, 'X')
    
    matrix = []
    for i in range(num_rows):
        row = padded_text[i * num_cols:(i + 1) * num_cols]
        matrix.append(list(row))
    
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    
    ciphertext = ""
    for col_idx in key_order:
        for row in matrix:
            ciphertext += row[col_idx]
    
    return ciphertext, matrix, key_order

plaintext = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
key = "31524"

print("=" * 60)
print("АЛГОРИТМ ШИФРОВАНИЯ ПЕРЕСТАНОВКОЙ")
print("=" * 60)
print(f"\nИсходный текст: {plaintext}")
print(f"Ключ (порядок столбцов): {key}")

ciphertext, matrix, key_order = encrypt_transposition(plaintext, key)

print(f"\nПорядок чтения столбцов: {[int(key[i]) for i in key_order]}")
print("\nМатрица заполнения (по строкам):")
print("-" * 30)

for i, row in enumerate(matrix):
    print(f"  {''.join(row)}")

print("-" * 30)
print(f"\nЗашифрованный текст: {ciphertext}")

grouped = " ".join([ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)])
print(f"По группам по 5: {grouped}")
print("=" * 60)
