russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

print("Русский алфавит:")
for i, letter in enumerate(russian_alphabet):
    print(f"{i:2d}: {letter}")

print("\n\nПроверка расшифровки первого слова:")
encrypted_word = "ъьмгрхц"
key = "книга"

print(f"Зашифрованное слово: {encrypted_word}")
print(f"Ключ: {key}")

for i, char in enumerate(encrypted_word):
    char_pos = russian_alphabet.index(char)
    key_char = key[i % len(key)]
    key_pos = russian_alphabet.index(key_char)
    
    decrypted_pos = (char_pos - key_pos) % len(russian_alphabet)
    decrypted_char = russian_alphabet[decrypted_pos]
    
    print(f"{char} (поз {char_pos:2d}) - {key_char} (поз {key_pos:2d}) = {decrypted_char} (поз {decrypted_pos:2d})")

print("\n\nПроверка: если подарки это правильно:")
correct_word = "подарки"
print(f"Если правильное слово: {correct_word}")
for i, (enc_char, dec_char) in enumerate(zip(encrypted_word, correct_word)):
    enc_pos = russian_alphabet.index(enc_char)
    dec_pos = russian_alphabet.index(dec_char)
    key_pos = (enc_pos - dec_pos) % len(russian_alphabet)
    key_char = russian_alphabet[key_pos]
    print(f"{enc_char} (поз {enc_pos:2d}) → {dec_char} (поз {dec_pos:2d}): ключ {key_char} (поз {key_pos:2d})")
