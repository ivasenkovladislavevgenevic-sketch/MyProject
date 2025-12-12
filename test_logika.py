def vigenere_decrypt(ciphertext, key):
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


ciphertext = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

# The pattern "лоигало" suggests "логика"
test_keys = ["логика", "лоигало", "лоигал", "логик"]

print(f"Зашифрованный текст: {ciphertext}\n")

for key in test_keys:
    result = vigenere_decrypt(ciphertext, key)
    print(f"Ключ '{key}': {result}")
