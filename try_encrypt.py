def vigenere_encrypt(plaintext, key):
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
    encrypted = []
    key_index = 0
    
    for char in plaintext:
        work_char = char.replace('ё', 'е').replace('Ё', 'Е')
        
        if work_char.lower() in russian_alphabet:
            char_pos = russian_alphabet.index(work_char.lower())
            key_char = key[key_index % len(key)].lower()
            key_pos = russian_alphabet.index(key_char)
            
            encrypted_pos = (char_pos + key_pos) % len(russian_alphabet)
            encrypted_char = russian_alphabet[encrypted_pos]
            
            if work_char.isupper():
                encrypted_char = encrypted_char.upper()
            
            encrypted.append(encrypted_char)
            key_index += 1
        else:
            encrypted.append(char)
    
    return ''.join(encrypted)


key = "книга"
text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

# Maybe they want encryption?
print("Шифрование с ключом 'книга':")
encrypted = vigenere_encrypt(text, key)
print(encrypted)

# Or maybe the given text should be interpreted differently
print("\nЕсли попробовать расшифровать распространенные фразы:")
common_phrases = [
    "подарки на новый год будут бесплатные",
    "поздравляю с новым годом",
    "счастливого нового года"
]

for phrase in common_phrases:
    enc = vigenere_encrypt(phrase, key)
    print(f"\n'{phrase}'")
    print(f"зашифровано: {enc}")
    print(f"оригинал:    {text}")
    print(f"совпадает: {enc == text}")
