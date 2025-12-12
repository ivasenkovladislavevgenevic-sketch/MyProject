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

key = "книга"
expected_plain = "подарки на новый год будут бесплатные"
actual_cipher = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

# Encrypt the expected plaintext
my_cipher = vigenere_encrypt(expected_plain, key)

print("Expected plaintext:", expected_plain)
print("My encryption:    ", my_cipher)
print("Actual ciphertext:", actual_cipher)
print()

# Compare character by character
print("Differences:")
for i, (m, a) in enumerate(zip(my_cipher, actual_cipher)):
    if m != a:
        context_start = max(0, i-5)
        context_end = min(len(my_cipher), i+6)
        print(f"Position {i}: '{m}' vs '{a}'")
        print(f"  Context: ...{my_cipher[context_start:context_end]}...")
        print(f"           ...{actual_cipher[context_start:context_end]}...")
