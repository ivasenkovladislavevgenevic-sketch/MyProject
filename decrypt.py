def vigenere_decrypt(ciphertext, key):
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
    decrypted = []
    key_index = 0
    
    for char in ciphertext:
        if char.lower() in russian_alphabet:
            char_pos = russian_alphabet.index(char.lower())
            key_char = key[key_index % len(key)].lower()
            key_pos = russian_alphabet.index(key_char)
            
            decrypted_pos = (char_pos - key_pos) % len(russian_alphabet)
            decrypted_char = russian_alphabet[decrypted_pos]
            
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            
            decrypted.append(decrypted_char)
            key_index += 1
        else:
            decrypted.append(char)
    
    return ''.join(decrypted)


key = "книга"
encrypted_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

decrypted_text = vigenere_decrypt(encrypted_text, key)

print("Ключ:", key)
print("Зашифрованный текст:", encrypted_text)
print("Расшифрованный текст:", decrypted_text)
