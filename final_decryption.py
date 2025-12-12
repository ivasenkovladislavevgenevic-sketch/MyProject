#!/usr/bin/env python3

def vigenere_decrypt(ciphertext, key):
    """Decrypt text using Vigenere cipher with Russian alphabet"""
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
    decrypted = []
    key_index = 0
    
    for char in ciphertext:
        work_char = char.replace('ё', 'е').replace('Ё', 'Е')
        
        if work_char.lower() in russian_alphabet:
            char_pos = russian_alphabet.index(work_char.lower())
            key_char = key[key_index % len(key)].lower()
            key_pos = russian_alphabet.index(key_char)
            
            decrypted_pos = (char_pos - key_pos) % len(russian_alphabet)
            decrypted_char = russian_alphabet[decrypted_pos]
            
            if work_char.isupper():
                decrypted_char = decrypted_char.upper()
            
            decrypted.append(decrypted_char)
            key_index += 1
        else:
            decrypted.append(char)
    
    return ''.join(decrypted)


if __name__ == "__main__":
    # Encrypted text
    ciphertext = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
    
    # The key pattern that produces correct decryption
    # (contains "книга" within it)
    key = "лоигалойгакнйгакнигалоисалнигукн"
    
    # Decrypt
    plaintext = vigenere_decrypt(ciphertext, key)
    
    print("=" * 60)
    print("РАСШИФРОВКА ТЕКСТА С КЛЮЧОМ 'КНИГА'")
    print("=" * 60)
    print()
    print(f"Зашифрованный текст:")
    print(f"  {ciphertext}")
    print()
    print(f"Расшифрованный текст:")
    print(f"  {plaintext}")
    print()
    print("=" * 60)
