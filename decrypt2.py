def vigenere_encrypt(plaintext, key):
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
    encrypted = []
    key_index = 0
    
    for char in plaintext:
        if char.lower() in russian_alphabet:
            char_pos = russian_alphabet.index(char.lower())
            key_char = key[key_index % len(key)].lower()
            key_pos = russian_alphabet.index(key_char)
            
            encrypted_pos = (char_pos + key_pos) % len(russian_alphabet)
            encrypted_char = russian_alphabet[encrypted_pos]
            
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            
            encrypted.append(encrypted_char)
            key_index += 1
        else:
            encrypted.append(char)
    
    return ''.join(encrypted)


key = "книга"
encrypted_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

result = vigenere_encrypt(encrypted_text, key)

print("Ключ:", key)
print("Зашифрованный текст:", encrypted_text)
print("Результат (шифрование):", result)
