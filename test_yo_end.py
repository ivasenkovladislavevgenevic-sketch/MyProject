def vigenere_decrypt_yo_end(ciphertext, key):
    # Russian alphabet with ё at the end (some implementations do this)
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяё'
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
            result.append(decrypted_char)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

key = "книга"
actual_cipher = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

print("Decrypting with ё at the end of alphabet:")
print(vigenere_decrypt_yo_end(actual_cipher, key))

# Also try without ё at all (treat it as е)
def vigenere_decrypt_no_yo(ciphertext, key):
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    result = []
    key = key.lower()
    key_length = len(key)
    key_index = 0
    
    for char in ciphertext:
        char_lower = char.lower()
        if char_lower == 'ё':
            char_lower = 'е'
        if char_lower in russian_alphabet:
            char_pos = russian_alphabet.index(char_lower)
            key_char_pos = russian_alphabet.index(key[key_index % key_length])
            decrypted_pos = (char_pos - key_char_pos) % len(russian_alphabet)
            decrypted_char = russian_alphabet[decrypted_pos]
            result.append(decrypted_char)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

print("\nDecrypting with ё treated as е (32-letter alphabet):")
print(vigenere_decrypt_no_yo(actual_cipher, key))

# Try with standard ordering ё after е
def vigenere_decrypt_yo_after_e(ciphertext, key):
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
            result.append(decrypted_char)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

print("\nDecrypting with ё after е (33-letter alphabet):")
print(vigenere_decrypt_yo_after_e(actual_cipher, key))
