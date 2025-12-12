def vigenere_decrypt(ciphertext, key):
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
    result = []
    key = key.lower()
    key_length = len(key)
    key_index = 0
    
    print(f"Alphabet length: {len(russian_alphabet)}")
    print(f"Key: {key}")
    print(f"Key positions: {[russian_alphabet.index(c) for c in key]}")
    print()
    
    for i, char in enumerate(ciphertext):
        char_lower = char.lower()
        if char_lower == 'ё':
            char_lower = 'е'
            
        if char_lower in russian_alphabet:
            char_pos = russian_alphabet.index(char_lower)
            key_char = key[key_index % key_length]
            key_char_pos = russian_alphabet.index(key_char)
            decrypted_pos = (char_pos - key_char_pos) % len(russian_alphabet)
            decrypted_char = russian_alphabet[decrypted_pos]
            
            print(f"{char} (pos {char_pos}) - {key_char} (pos {key_char_pos}) = {decrypted_char} (pos {decrypted_pos})")
            
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            result.append(decrypted_char)
            key_index += 1
        else:
            result.append(char)
            print(f"'{char}' - keeping as is")
    
    return ''.join(result)

encrypted_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
key = "книга"
print("=" * 60)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("=" * 60)
print()
print("Зашифрованный текст:", encrypted_text)
print("Ключ:", key)
print("Расшифрованный текст:", decrypted_text)
