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

# We know that:
# - "на новыйгод" appears with key "кнйга"
# - We need to find what makes "подарки" and "будут" and "бесплатные" appear

# Let's check what the first word needs
# Encrypted: ъьмгрхц
# Expected: подарки

russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

encrypted_first = "ъьмгрхц"
expected_first = "подарки"

print("Вычисляем ключ из первого слова:")
key_chars = []
for i, (enc, exp) in enumerate(zip(encrypted_first, expected_first)):
    enc_pos = russian_alphabet.index(enc)
    exp_pos = russian_alphabet.index(exp)
    key_pos = (enc_pos - exp_pos) % len(russian_alphabet)
    key_char = russian_alphabet[key_pos]
    key_chars.append(key_char)
    print(f"{enc} ({enc_pos:2d}) → {exp} ({exp_pos:2d}): ключ = {key_char} (поз {key_pos:2d})")

potential_key = ''.join(key_chars)
print(f"\nПотенциальный ключ: {potential_key}")

# Test this key
result = vigenere_decrypt(ciphertext, potential_key)
print(f"Результат с этим ключом: {result}")
