def vigenere_decrypt_all_chars(ciphertext, key):
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
    decrypted = []
    
    for i, char in enumerate(ciphertext):
        work_char = char.replace('ё', 'е').replace('Ё', 'Е')
        
        if work_char.lower() in russian_alphabet:
            char_pos = russian_alphabet.index(work_char.lower())
            key_char = key[i % len(key)].lower()
            
            if key_char in russian_alphabet:
                key_pos = russian_alphabet.index(key_char)
                decrypted_pos = (char_pos - key_pos) % len(russian_alphabet)
                decrypted_char = russian_alphabet[decrypted_pos]
                
                if work_char.isupper():
                    decrypted_char = decrypted_char.upper()
                
                decrypted.append(decrypted_char)
            else:
                decrypted.append(char)
        else:
            decrypted.append(char)
    
    return ''.join(decrypted)


key = "книга"
encrypted_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

print("Попытка 1: ключ только по буквам")
russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
decrypted = []
key_index = 0
for char in encrypted_text:
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
result1 = ''.join(decrypted)
print("Результат:", result1)

print("\nПопытка 2: ключ по всем символам")
result2 = vigenere_decrypt_all_chars(encrypted_text, key)
print("Результат:", result2)
