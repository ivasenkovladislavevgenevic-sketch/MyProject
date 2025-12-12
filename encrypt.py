#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Алгоритм шифрования перестановкой (столбцовая перестановка)
"""

def columnar_transposition_encrypt(text, key):
    """
    Шифрует текст методом столбцовой перестановки
    
    Args:
        text: исходный текст (без пробелов)
        key: ключ для перестановки столбцов
    
    Returns:
        зашифрованный текст
    """
    # Удаляем пробелы и приводим к верхнему регистру
    text = text.replace(' ', '').upper()
    
    # Определяем порядок столбцов на основе ключа
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    
    # Определяем количество столбцов (равно длине ключа)
    num_cols = len(key)
    
    # Определяем количество строк
    num_rows = (len(text) + num_cols - 1) // num_cols
    
    # Создаем матрицу и заполняем текстом
    matrix = []
    text_index = 0
    
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            if text_index < len(text):
                row.append(text[text_index])
                text_index += 1
            else:
                row.append('')  # Заполнитель для неполных строк
        matrix.append(row)
    
    # Читаем по столбцам в порядке, определенном ключом
    encrypted = []
    for col_idx in key_order:
        for row in matrix:
            if row[col_idx]:
                encrypted.append(row[col_idx])
    
    return ''.join(encrypted)


def columnar_transposition_decrypt(encrypted_text, key):
    """
    Расшифровывает текст, зашифрованный методом столбцовой перестановки
    
    Args:
        encrypted_text: зашифрованный текст
        key: ключ для перестановки столбцов
    
    Returns:
        расшифрованный текст
    """
    # Определяем порядок столбцов на основе ключа
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    
    num_cols = len(key)
    total_chars = len(encrypted_text)
    num_rows = (total_chars + num_cols - 1) // num_cols
    
    # Определяем количество символов в каждом столбце
    # Первые (total_chars % num_cols) столбцов имеют num_rows символов
    # Остальные имеют (num_rows - 1) символов
    chars_per_col = [num_rows] * num_cols
    remainder = total_chars % num_cols
    if remainder > 0:
        for i in range(remainder, num_cols):
            chars_per_col[key_order[i]] = num_rows - 1
    
    # Создаем пустую матрицу
    matrix = [[''] * num_cols for _ in range(num_rows)]
    
    # Заполняем матрицу по столбцам в порядке ключа
    text_index = 0
    for col_idx in key_order:
        num_chars = chars_per_col[col_idx]
        for row_idx in range(num_chars):
            if text_index < len(encrypted_text):
                matrix[row_idx][col_idx] = encrypted_text[text_index]
                text_index += 1
    
    # Читаем по строкам
    decrypted = []
    for row in matrix:
        for char in row:
            if char:
                decrypted.append(char)
    
    return ''.join(decrypted)


if __name__ == "__main__":
    # Исходный текст
    original_text = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
    
    # Ключ для перестановки (можно использовать любое слово или последовательность)
    # Длина ключа определяет количество столбцов
    key = "КЛЮЧ"
    
    print("=" * 60)
    print("ШИФРОВАНИЕ ПЕРЕСТАНОВКОЙ")
    print("=" * 60)
    print(f"\nИсходный текст:")
    print(original_text)
    print(f"\nТекст без пробелов:")
    text_no_spaces = original_text.replace(' ', '')
    print(text_no_spaces)
    print(f"\nКлюч: {key}")
    print(f"Длина ключа (количество столбцов): {len(key)}")
    
    # Шифруем
    encrypted = columnar_transposition_encrypt(original_text, key)
    print(f"\nЗашифрованный текст:")
    print(encrypted)
    
    # Показываем процесс шифрования
    print(f"\n" + "=" * 60)
    print("ПРОЦЕСС ШИФРОВАНИЯ:")
    print("=" * 60)
    
    text = original_text.replace(' ', '').upper()
    num_cols = len(key)
    num_rows = (len(text) + num_cols - 1) // num_cols
    
    print(f"\nМатрица ({num_rows} строк × {num_cols} столбцов):")
    print(f"Ключ: {key}")
    print(f"Порядок столбцов (по алфавиту ключа): {sorted(range(len(key)), key=lambda k: key[k])}")
    
    # Создаем матрицу для отображения
    matrix = []
    text_index = 0
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            if text_index < len(text):
                row.append(text[text_index])
                text_index += 1
            else:
                row.append('')
        matrix.append(row)
    
    # Выводим матрицу
    print("\nИсходная матрица (запись по строкам):")
    print("  " + " ".join([f"{i+1}" for i in range(num_cols)]))
    for i, row in enumerate(matrix):
        print(f"{i+1} " + " ".join([char if char else ' ' for char in row]))
    
    # Выводим порядок чтения столбцов
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    print(f"\nЧтение столбцов в порядке: {key_order}")
    print("(столбцы читаются сверху вниз)")
    
    # Проверяем расшифровку
    print(f"\n" + "=" * 60)
    print("ПРОВЕРКА РАСШИФРОВКИ:")
    print("=" * 60)
    decrypted = columnar_transposition_decrypt(encrypted, key)
    print(f"\nРасшифрованный текст:")
    print(decrypted)
    print(f"\nСовпадает с исходным: {decrypted == text_no_spaces}")
