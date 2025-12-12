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
original_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

test_phrases = [
    "подарки на новыйгод будут бесплатные",
    "подарки на новыйгод будут бесплатныё",
    "подарки на новый год будут бесплатные",
    "подарки но новыйгод будут бесплатные",
]

print("Оригинал:", original_text)
print()

for phrase in test_phrases:
    enc = vigenere_encrypt(phrase, key)
    match = "✓✓✓ СОВПАДЕНИЕ!" if enc == original_text else ""
    print(f"Фраза: {phrase}")
    print(f"Шифр:  {enc}")
    print(f"       {match}")
    
    # Check character by character
    if len(enc) == len(original_text):
        diff_count = sum(1 for a, b in zip(enc, original_text) if a != b)
        print(f"       Различий: {diff_count} из {len(enc)} символов")
    print()
