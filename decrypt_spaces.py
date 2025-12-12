def vigenere_decrypt_with_spaces(ciphertext, key):
    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = []
    key = key.lower()
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        char_lower = char.lower()
        if char_lower in russian_alphabet:
            char_pos = russian_alphabet.index(char_lower)
            key_char_pos = russian_alphabet.index(key[i % key_length])
            decrypted_pos = (char_pos - key_char_pos) % len(russian_alphabet)
            decrypted_char = russian_alphabet[decrypted_pos]
            result.append(decrypted_char)
        else:
            result.append(char)
    return ''.join(result)

key = "книга"
actual_cipher = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

print("Decrypting with spaces advancing key (33-letter alphabet):")
print(vigenere_decrypt_with_spaces(actual_cipher, key))
