#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def encrypt_transposition(text, key):
    text = text.replace(' ', '')
    rows = (len(text) + key - 1) // key
    matrix = []
    for i in range(rows):
        start = i * key
        end = start + key
        row = list(text[start:end])
        while len(row) < key:
            row.append(' ')
        matrix.append(row)
    encrypted = []
    for col in range(key):
        for row in range(rows):
            encrypted.append(matrix[row][col])
    return ''.join(encrypted).strip()

def decrypt_transposition(encrypted_text, key):
    rows = (len(encrypted_text) + key - 1) // key
    matrix = [[' ' for _ in range(key)] for _ in range(rows)]
    idx = 0
    for col in range(key):
        for row in range(rows):
            if idx < len(encrypted_text):
                matrix[row][col] = encrypted_text[idx]
                idx += 1
    decrypted = []
    for row in range(rows):
        for col in range(key):
            decrypted.append(matrix[row][col])
    return ''.join(decrypted).strip()

if __name__ == "__main__":
    original_text = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
    key = 7
    print("=" * 60)
    print("АЛГОРИТМ ПЕРЕСТАНОВКИ (СТОЛБЦОВАЯ ПЕРЕСТАНОВКА)")
    print("=" * 60)
    print(f"\nИсходный текст:")
    print(original_text)
    print(f"\nКлюч (количество столбцов): {key}")
    encrypted = encrypt_transposition(original_text, key)
    print(f"\nЗашифрованный текст:")
    print(encrypted)
    decrypted = decrypt_transposition(encrypted, key)
    print(f"\nРасшифрованный текст (для проверки):")
    print(decrypted.replace(' ', ' '))
    print("\n" + "=" * 60)
