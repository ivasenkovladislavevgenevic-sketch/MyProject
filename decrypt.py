# -*- coding: utf-8 -*-
def decrypt_vigenere(ciphertext, key):
    # Russian alphabet including ё
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    key = key.lower()
    ciphertext = ciphertext.lower()
    
    plaintext = []
    key_index = 0
    key_length = len(key)
    
    for char in ciphertext:
        if char in alphabet:
            char_index = alphabet.index(char)
            key_char = key[key_index % key_length]
            key_char_index = alphabet.index(key_char)
            
            plain_index = (char_index - key_char_index) % len(alphabet)
            plaintext.append(alphabet[plain_index])
            
            key_index += 1
        else:
            plaintext.append(char)
            
    return "".join(plaintext)

cipher = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
key = "книга"

print("Decrypted:", decrypt_vigenere(cipher, key))
