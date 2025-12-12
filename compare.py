def vigenere_encrypt(plaintext, key):
    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = []
    key = key.lower()
    key_length = len(key)
    key_index = 0
    
    for char in plaintext:
        char_lower = char.lower()
        if char_lower in russian_alphabet:
            char_pos = russian_alphabet.index(char_lower)
            key_char_pos = russian_alphabet.index(key[key_index % key_length])
            encrypted_pos = (char_pos + key_char_pos) % len(russian_alphabet)
            encrypted_char = russian_alphabet[encrypted_pos]
            result.append(encrypted_char)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decrypt(ciphertext, key):
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

key = "книга"
actual_cipher = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

# Try decrypting with different possible keys
print("Decrypting with key 'книга':")
print(vigenere_decrypt(actual_cipher, key))
print()

# Let's also try without ё in the alphabet
russian_alphabet_no_yo = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def decrypt_no_yo(ciphertext, key):
    result = []
    key = key.lower()
    key_length = len(key)
    key_index = 0
    
    for char in ciphertext:
        char_lower = char.lower()
        if char_lower == 'ё':
            char_lower = 'е'
        if char_lower in russian_alphabet_no_yo:
            char_pos = russian_alphabet_no_yo.index(char_lower)
            key_char_pos = russian_alphabet_no_yo.index(key[key_index % key_length])
            decrypted_pos = (char_pos - key_char_pos) % len(russian_alphabet_no_yo)
            decrypted_char = russian_alphabet_no_yo[decrypted_pos]
            result.append(decrypted_char)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

print("Decrypting with 32-letter alphabet (no ё):")
print(decrypt_no_yo(actual_cipher, key))
