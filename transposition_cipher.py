#!/usr/bin/env python3

def columnar_transposition_encrypt(plaintext, key):
    """
    Encrypt text using columnar transposition cipher
    """
    # Remove spaces from plaintext
    plaintext = plaintext.replace(' ', '')
    
    # Create key order (numbered positions based on alphabetical order)
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    key_indices = [x[0] for x in key_order]
    
    # Number of columns = length of key
    num_cols = len(key)
    
    # Number of rows needed
    num_rows = (len(plaintext) + num_cols - 1) // num_cols
    
    # Pad the plaintext if necessary
    padded_length = num_rows * num_cols
    plaintext_padded = plaintext.ljust(padded_length, 'Я')
    
    # Create the grid
    grid = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            idx = i * num_cols + j
            if idx < len(plaintext_padded):
                row.append(plaintext_padded[idx])
            else:
                row.append('Я')
        grid.append(row)
    
    # Read columns in key order
    ciphertext = ''
    for col_idx in key_indices:
        for row in grid:
            ciphertext += row[col_idx]
    
    return ciphertext


def columnar_transposition_decrypt(ciphertext, key):
    """
    Decrypt text using columnar transposition cipher
    """
    # Create key order
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    key_indices = [x[0] for x in key_order]
    
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    
    # Reconstruct grid by reading columns in key order
    grid = [[''] * num_cols for _ in range(num_rows)]
    
    char_idx = 0
    for col_idx in key_indices:
        for row_idx in range(num_rows):
            grid[row_idx][col_idx] = ciphertext[char_idx]
            char_idx += 1
    
    # Read row by row
    plaintext = ''
    for row in grid:
        plaintext += ''.join(row)
    
    # Remove padding
    plaintext = plaintext.rstrip('Я')
    
    return plaintext


if __name__ == "__main__":
    # Text to encrypt
    plaintext = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
    
    # Key for transposition
    key = "КНИГА"
    
    print("=" * 70)
    print("ШИФРОВАНИЕ МЕТОДОМ ПЕРЕСТАНОВКИ (COLUMNAR TRANSPOSITION)")
    print("=" * 70)
    print()
    print(f"Исходный текст:")
    print(f"  {plaintext}")
    print()
    print(f"Ключ: {key}")
    print()
    
    # Encrypt
    ciphertext = columnar_transposition_encrypt(plaintext, key)
    print(f"Зашифрованный текст:")
    print(f"  {ciphertext}")
    print()
    
    # Show the grid for visualization
    plaintext_no_spaces = plaintext.replace(' ', '')
    num_cols = len(key)
    num_rows = (len(plaintext_no_spaces) + num_cols - 1) // num_cols
    padded = plaintext_no_spaces.ljust(num_rows * num_cols, 'Я')
    
    print("Таблица шифрования:")
    print(f"  Ключ: {' '.join(key)}")
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    order_nums = [''] * len(key)
    for new_idx, (orig_idx, _) in enumerate(key_order):
        order_nums[orig_idx] = str(new_idx + 1)
    print(f"  Порядок: {' '.join(order_nums)}")
    print()
    
    for i in range(num_rows):
        row_chars = []
        for j in range(num_cols):
            idx = i * num_cols + j
            if idx < len(padded):
                row_chars.append(padded[idx])
        print(f"  {' '.join(row_chars)}")
    
    print()
    print("=" * 70)
    
    # Verify decryption
    decrypted = columnar_transposition_decrypt(ciphertext, key)
    print(f"\nПроверка расшифровки: {decrypted}")
    print(f"Совпадает с оригиналом: {decrypted == plaintext.replace(' ', '')}")
