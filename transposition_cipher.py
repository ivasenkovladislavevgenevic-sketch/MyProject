#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def encrypt_transposition(plaintext, key):
    text = plaintext.replace(" ", "")
    num_columns = key
    num_rows = math.ceil(len(text) / num_columns)
    padded_text = text + 'Х' * (num_rows * num_columns - len(text))
    
    print(f"\nИсходный текст: {plaintext}")
    print(f"Текст без пробелов: {text}")
    print(f"Длина текста: {len(text)}")
    print(f"Ключ (столбцов): {key}")
    print(f"Количество строк: {num_rows}")
    
    table = []
    print("\nТаблица перестановки:")
    print("-" * (num_columns * 3 + 1))
    for i in range(num_rows):
        row = padded_text[i * num_columns : (i + 1) * num_columns]
        table.append(row)
        print("|" + "|".join(f"{c}" for c in row) + "|")
    print("-" * (num_columns * 3 + 1))
    
    ciphertext = ""
    for col in range(num_columns):
        for row in range(num_rows):
            ciphertext += table[row][col]
    
    return ciphertext

original_text = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
key = 7

print("=" * 60)
print("ШИФР ПЕРЕСТАНОВКИ (КОЛОННАЯ ТРАНСПОЗИЦИЯ)")
print("=" * 60)

encrypted = encrypt_transposition(original_text, key)
print(f"\n*** ЗАШИФРОВАННЫЙ ТЕКСТ ***")
print(f"{encrypted}")

print("\n" + "=" * 60)
print("ВАРИАНТ С КЛЮЧОМ 6:")
print("=" * 60)
encrypted2 = encrypt_transposition(original_text, 6)
print(f"\n*** ЗАШИФРОВАННЫЙ ТЕКСТ ***")
print(f"{encrypted2}")
