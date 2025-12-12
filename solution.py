#!/usr/bin/env python3
"""
Расшифровка текста шифром Виженера с ключом "книга"
"""

def vigenere_decrypt(ciphertext, key):
    """
    Расшифровка текста с использованием шифра Виженера
    
    Параметры:
        ciphertext: зашифрованный текст
        key: ключевое слово для расшифровки
        
    Возвращает:
        расшифрованный текст
    """
    # Русский алфавит с буквой ё (33 буквы)
    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    result = []
    key_index = 0
    key_lower = key.lower()
    
    for char in ciphertext.lower():
        # Пробелы сохраняем как есть
        if char == ' ':
            result.append(' ')
            continue
            
        # Расшифровываем только буквы из алфавита
        if char in russian_alphabet:
            # Находим позицию символа в алфавите
            char_pos = russian_alphabet.index(char)
            
            # Находим соответствующий символ ключа
            key_char = key_lower[key_index % len(key_lower)]
            
            if key_char in russian_alphabet:
                key_pos = russian_alphabet.index(key_char)
            else:
                result.append(char)
                continue
            
            # Применяем формулу расшифровки Виженера
            decrypted_pos = (char_pos - key_pos) % len(russian_alphabet)
            result.append(russian_alphabet[decrypted_pos])
            
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)


def main():
    # Исходные данные
    encrypted_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
    key = "книга"
    
    print("=" * 70)
    print("РАСШИФРОВКА ТЕКСТА С ШИФРОМ ВИЖЕНЕРА")
    print("=" * 70)
    print()
    print(f"Зашифрованный текст: {encrypted_text}")
    print(f"Ключ: {key}")
    print()
    
    # Расшифровываем
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    
    print("РЕЗУЛЬТАТ:")
    print(f"Расшифрованный текст: {decrypted_text}")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()
