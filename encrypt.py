#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Шифрование текста алгоритмом перестановки
"""

def columnar_transposition_encrypt(plaintext, num_cols):
    """
    Простая столбцовая перестановка: запись по строкам, чтение по столбцам
    """
    text = plaintext.replace(" ", "")
    num_rows = (len(text) + num_cols - 1) // num_cols
    
    # Дополняем текст
    padded_text = text + 'Х' * (num_rows * num_cols - len(text))
    
    print("Исходный текст:", plaintext)
    print("Текст без пробелов:", text)
    print(f"Длина текста: {len(text)}")
    print(f"Размер матрицы: {num_rows} строк x {num_cols} столбцов")
    print()
    
    # Создаём и выводим матрицу
    print("Матрица (запись по строкам):")
    matrix = []
    for i in range(num_rows):
        row = padded_text[i * num_cols : (i + 1) * num_cols]
        matrix.append(row)
        print(f"  {row}")
    print()
    
    # Читаем по столбцам
    ciphertext = ""
    for col in range(num_cols):
        for row in range(num_rows):
            ciphertext += matrix[row][col]
    
    return ciphertext


# Исходный текст
plaintext = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"

print("=" * 70)
print("ШИФРОВАНИЕ АЛГОРИТМОМ ПЕРЕСТАНОВКИ")
print("=" * 70)
print()

# Столбцовая перестановка с 7 столбцами
ciphertext = columnar_transposition_encrypt(plaintext, 7)

print("ЗАШИФРОВАННЫЙ ТЕКСТ:")
print(ciphertext)
print()

# Разбиваем на блоки для читаемости
print("Зашифрованный текст (блоками по 7):")
for i in range(0, len(ciphertext), 7):
    print(ciphertext[i:i+7], end=" ")
print()
