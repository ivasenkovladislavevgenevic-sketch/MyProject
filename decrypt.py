#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decrypt_vigenere(ciphertext, key):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_len = len(alphabet)
    char_to_pos = {char: i for i, char in enumerate(alphabet)}
    
    decrypted = []
    key_index = 0
    
    for char in ciphertext:
        if char.lower() in char_to_pos:
            cipher_pos = char_to_pos[char.lower()]
            key_pos = char_to_pos[key[key_index % len(key)].lower()]
            decrypted_pos = (cipher_pos - key_pos) % alphabet_len
            decrypted_char = alphabet[decrypted_pos]
            if char.isupper():
                decrypted.append(decrypted_char.upper())
            else:
                decrypted.append(decrypted_char)
            key_index += 1
        else:
            decrypted.append(char)
    
    return ''.join(decrypted)

ciphertext = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
key = "книга"

decrypted = decrypt_vigenere(ciphertext, key)
print(f"Зашифрованный текст: {ciphertext}")
print(f"Ключ: {key}")
print(f"Расшифрованный текст: {decrypted}")
