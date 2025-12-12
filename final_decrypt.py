#!/usr/bin/env python3

def vigenere_decrypt(ciphertext, key):
    """
    Decrypt text using Vigenere cipher with Russian alphabet (33 letters, including ё)
    """
    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    result = []
    key = key.lower()
    key_length = len(key)
    key_index = 0
    
    for char in ciphertext:
        char_lower = char.lower()
        if char_lower in russian_alphabet:
            char_pos = russian_alphabet.index(char_lower)
            key_char_pos = russian_alphabet.index(key[key_index % key_length])
            decrypted_pos = (char_pos - key_char_pos) % len(russian_alphabet)
            decrypted_char = russian_alphabet[decrypted_pos]
            result.append(decrypted_char)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    ciphertext = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
    key = "книга"
    
    decrypted = vigenere_decrypt(ciphertext, key)
    
    print("="*60)
    print("РАСШИФРОВКА ТЕКСТА")
    print("="*60)
    print()
    print(f"Зашифрованный текст: {ciphertext}")
    print(f"Ключ: {key}")
    print()
    print(f"Расшифрованный текст: {decrypted}")
    print()
    print("="*60)
