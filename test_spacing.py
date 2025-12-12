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

# Try different spacing variations
test_plaintexts = [
    "подарки на новыйгод будут бесплатные",
    "подарки на новый год будут бесплатные",
    "подарки на новый годбудут бесплатные",
    "подарки нановый год будут бесплатные"
]

print("Testing different spacing variations:")
for plain in test_plaintexts:
    encrypted = vigenere_encrypt(plain, key)
    match = "✓" if encrypted == actual_cipher else "✗"
    print(f"{match} {plain}")
    if encrypted == actual_cipher:
        print(f"   MATCH! This is the correct plaintext!")
    else:
        print(f"   Got: {encrypted}")

print("\n" + "="*60)
print("Decrypting actual ciphertext:")
decrypted = vigenere_decrypt(actual_cipher, key)
print(f"Result: {decrypted}")
