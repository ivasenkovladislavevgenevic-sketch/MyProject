#!/usr/bin/env python3
"""
Скрипт для расшифровки текста с использованием книжного шифра (метод Виженера)
"""

def decrypt_vigenere(encrypted_text, book_text):
    """
    Расшифровка методом Виженера с использованием книги как ключа
    
    Args:
        encrypted_text: зашифрованный текст
        book_text: текст книги-ключа
    
    Returns:
        расшифрованный текст
    """
    # Убираем пробелы из зашифрованного текста для обработки
    encrypted_clean = encrypted_text.replace(' ', '')
    # Сохраняем позиции пробелов
    space_positions = [i for i, c in enumerate(encrypted_text) if c == ' ']
    
    # Извлекаем только русские буквы из книги
    key_clean = ''.join([c for c in book_text.lower() if 'а' <= c <= 'я'])
    
    if not key_clean:
        return "Ошибка: книга не содержит русских букв"
    
    decrypted = []
    key_index = 0
    
    for char in encrypted_clean:
        if 'а' <= char <= 'я':
            # Позиция зашифрованной буквы в алфавите (0-32)
            enc_pos = ord(char) - ord('а')
            # Берем букву из ключа (циклически)
            key_char = key_clean[key_index % len(key_clean)]
            key_pos = ord(key_char) - ord('а')
            
            # Расшифровка: decrypted = (encrypted - key) mod 33
            dec_pos = (enc_pos - key_pos) % 33
            decrypted_char = chr(ord('а') + dec_pos)
            decrypted.append(decrypted_char)
            
            key_index += 1
        else:
            decrypted.append(char)
    
    # Восстанавливаем пробелы
    result = list(''.join(decrypted))
    for pos in reversed(space_positions):
        if pos <= len(result):
            result.insert(pos, ' ')
    
    return ''.join(result)


def decrypt_from_file(encrypted_text, book_file_path):
    """Читает книгу из файла и расшифровывает"""
    try:
        with open(book_file_path, 'r', encoding='utf-8') as f:
            book_text = f.read()
        return decrypt_vigenere(encrypted_text, book_text)
    except Exception as e:
        return f"Ошибка при чтении файла: {e}"


if __name__ == "__main__":
    encrypted = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
    
    print("Зашифрованный текст:", encrypted)
    print("\n" + "="*70)
    print("Для расшифровки нужен текст книги-ключа.")
    print("\nИспользование:")
    print("  1. С текстом книги:")
    print("     decrypt_vigenere(encrypted, 'текст вашей книги здесь')")
    print("\n  2. С файлом книги:")
    print("     decrypt_from_file(encrypted, 'путь/к/книге.txt')")
    print("\n" + "="*70)
