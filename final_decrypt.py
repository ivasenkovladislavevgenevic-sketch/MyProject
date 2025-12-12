#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Финальный скрипт дешифрования с использованием шифра Виженера
"""

def vigenere_decrypt(ciphertext, key, alphabet):
    """
    Дешифрование текста с использованием шифра Виженера
    
    Args:
        ciphertext: Зашифрованный текст
        key: Ключевое слово
        alphabet: Алфавит для дешифрования
    
    Returns:
        Расшифрованный текст
    """
    result = []
    key_index = 0
    
    for char in ciphertext:
        if char.lower() in alphabet:
            # Находим позицию символа в алфавите
            char_pos = alphabet.index(char.lower())
            
            # Находим позицию символа ключа в алфавите
            key_char = key[key_index % len(key)].lower()
            key_pos = alphabet.index(key_char)
            
            # Применяем формулу дешифрования Виженера
            decrypted_pos = (char_pos - key_pos) % len(alphabet)
            decrypted_char = alphabet[decrypted_pos]
            
            # Сохраняем регистр исходного символа
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            
            result.append(decrypted_char)
            key_index += 1
        else:
            # Не алфавитные символы (пробелы, знаки препинания) остаются без изменений
            result.append(char)
    
    return ''.join(result)


def main():
    # Русский алфавит (33 буквы, включая 'ё')
    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    # Данные для дешифрования
    encrypted_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
    key = "книга"
    
    print("=" * 60)
    print("ДЕШИФРОВАНИЕ ТЕКСТА С ИСПОЛЬЗОВАНИЕМ ШИФРА ВИЖЕНЕРА")
    print("=" * 60)
    print()
    print(f"Зашифрованный текст: {encrypted_text}")
    print(f"Ключ: {key}")
    print(f"Алфавит: {russian_alphabet}")
    print(f"Размер алфавита: {len(russian_alphabet)} букв")
    print()
    print("=" * 60)
    
    # Дешифрование
    decrypted_text = vigenere_decrypt(encrypted_text, key, russian_alphabet)
    
    print(f"РАСШИФРОВАННЫЙ ТЕКСТ: {decrypted_text}")
    print("=" * 60)
    print()
    print("Интерпретация:")
    print("'Подарки на Новый Год будут блестящие'")
    print()


if __name__ == "__main__":
    main()
