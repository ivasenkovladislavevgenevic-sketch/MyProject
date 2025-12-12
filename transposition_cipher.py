#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def columnar_transposition_encrypt(text, key):
    text_clean = text.replace(' ', '')
    
    if isinstance(key, int):
        num_cols = key
        num_rows = (len(text_clean) + num_cols - 1) // num_cols
        
        matrix = []
        for i in range(num_rows):
            start = i * num_cols
            end = start + num_cols
            row = list(text_clean[start:end])
            while len(row) < num_cols:
                row.append(' ')
            matrix.append(row)
        
        encrypted = ''
        for col in range(num_cols):
            for row in range(num_rows):
                encrypted += matrix[row][col]
        
        return encrypted.replace(' ', '')
    else:
        num_cols = len(key)
        num_rows = (len(text_clean) + num_cols - 1) // num_cols
        
        matrix = []
        for i in range(num_rows):
            start = i * num_cols
            end = start + num_cols
            row = list(text_clean[start:end])
            while len(row) < num_cols:
                row.append(' ')
            matrix.append(row)
        
        key_order = sorted(range(num_cols), key=lambda x: key[x])
        
        encrypted = ''
        for col_idx in key_order:
            for row in range(num_rows):
                encrypted += matrix[row][col_idx]
        
        return encrypted.replace(' ', '')


def rail_fence_encrypt(text, rails=3):
    text_clean = text.replace(' ', '')
    
    fence = [[''] * len(text_clean) for _ in range(rails)]
    
    direction = 1
    row = 0
    
    for i, char in enumerate(text_clean):
        fence[row][i] = char
        row += direction
        
        if row == rails - 1 or row == 0:
            direction *= -1
    
    encrypted = ''
    for r in range(rails):
        encrypted += ''.join(fence[r])
    
    return encrypted


if __name__ == "__main__":
    plaintext = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
    
    print("Исходный текст:")
    print(plaintext)
    print("\n" + "="*60 + "\n")
    
    print("1. Столбцовая перестановка (5 столбцов):")
    encrypted1 = columnar_transposition_encrypt(plaintext, 5)
    print(encrypted1)
    print(f"Длина: {len(encrypted1)} символов\n")
    
    print("2. Столбцовая перестановка (ключ 'КРИПТО'):")
    key = "КРИПТО"
    encrypted2 = columnar_transposition_encrypt(plaintext, key)
    print(encrypted2)
    print(f"Длина: {len(encrypted2)} символов\n")
    
    print("3. Rail Fence (3 рельса):")
    encrypted3 = rail_fence_encrypt(plaintext, 3)
    print(encrypted3)
    print(f"Длина: {len(encrypted3)} символов\n")
    
    print("4. Rail Fence (4 рельса):")
    encrypted4 = rail_fence_encrypt(plaintext, 4)
    print(encrypted4)
    print(f"Длина: {len(encrypted4)} символов\n")
    
    with open('encrypted_output.txt', 'w', encoding='utf-8') as f:
        f.write("Исходный текст:\n")
        f.write(plaintext + "\n\n")
        f.write("="*60 + "\n\n")
        f.write("1. Столбцовая перестановка (5 столбцов):\n")
        f.write(encrypted1 + "\n\n")
        f.write("2. Столбцовая перестановка (ключ 'КРИПТО'):\n")
        f.write(encrypted2 + "\n\n")
        f.write("3. Rail Fence (3 рельса):\n")
        f.write(encrypted3 + "\n\n")
        f.write("4. Rail Fence (4 рельса):\n")
        f.write(encrypted4 + "\n")
    
    print("Результаты сохранены в файл 'encrypted_output.txt'")
