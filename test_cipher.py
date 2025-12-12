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
            if char.isupper():
                encrypted_char = encrypted_char.upper()
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
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            result.append(decrypted_char)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

# Test with a known phrase
key = "книга"
test_plain = "подарки на новый год будут бесплатные"
print("Test encryption/decryption:")
print(f"Original: {test_plain}")

encrypted = vigenere_encrypt(test_plain, key)
print(f"Encrypted: {encrypted}")

decrypted = vigenere_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
print()

# Now decrypt the actual ciphertext
encrypted_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
print("Actual ciphertext:")
print(f"Ciphertext: {encrypted_text}")
decrypted_text = vigenere_decrypt(encrypted_text, key)
print(f"Decrypted: {decrypted_text}")
