def vigenere_decrypt(ciphertext, key):
    # Russian alphabet with ё (33 letters)
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
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            result.append(decrypted_char)
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

encrypted_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
key = "книга"
decrypted_text = vigenere_decrypt(encrypted_text, key)

print("Зашифрованный текст:", encrypted_text)
print("Ключ:", key)
print("Расшифрованный текст:", decrypted_text)
print()
print(f"Длина алфавита: {len('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')}")
