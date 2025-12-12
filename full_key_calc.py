russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# Most likely plaintext (our best guess)
ciphertext = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
plaintext_guess = "подарки на новыйгод будут бесплатные"

print(f"Зашифрованный: {ciphertext}")
print(f"Предполагаемый: {plaintext_guess}")
print()

if len(plaintext_guess.replace(' ', '').replace('ё', 'е')) == len(ciphertext.replace(' ', '').replace('ё', 'е')):
    print("Длины совпадают (без учета пробелов)")
else:
    print("Длины НЕ совпадают!")
    print(f"Шифр: {len(ciphertext.replace(' ', ''))} символов")
    print(f"Текст: {len(plaintext_guess.replace(' ', ''))} символов")

print()
print("Вычисляем ключ:")

key_chars = []
plain_idx = 0

for cipher_char in ciphertext:
    # Skip spaces in plaintext to match cipher
    while plain_idx < len(plaintext_guess) and plaintext_guess[plain_idx] == ' ':
        plain_idx += 1
    
    if plain_idx >= len(plaintext_guess):
        break
        
    plain_char = plaintext_guess[plain_idx].replace('ё', 'е')
    cipher_work = cipher_char.replace('ё', 'е')
    
    if cipher_char == ' ':
        key_chars.append(' ')
        continue
    
    if cipher_work.lower() in russian_alphabet and plain_char.lower() in russian_alphabet:
        cipher_pos = russian_alphabet.index(cipher_work.lower())
        plain_pos = russian_alphabet.index(plain_char.lower())
        key_pos = (cipher_pos - plain_pos) % len(russian_alphabet)
        key_char = russian_alphabet[key_pos]
        key_chars.append(key_char)
        print(f"{cipher_char} ({cipher_pos:2d}) - {plain_char} ({plain_pos:2d}) = {key_char} (поз {key_pos:2d})")
    
    plain_idx += 1

full_key = ''.join(key_chars)
print(f"\nПолный ключ: {full_key}")

# Now test this key
def vigenere_decrypt(ciphertext, key):
    decrypted = []
    key_index = 0
    
    for char in ciphertext:
        work_char = char.replace('ё', 'е')
        
        if work_char.lower() in russian_alphabet:
            char_pos = russian_alphabet.index(work_char.lower())
            key_char = key[key_index % len(key)].lower()
            key_pos = russian_alphabet.index(key_char)
            
            decrypted_pos = (char_pos - key_pos) % len(russian_alphabet)
            decrypted_char = russian_alphabet[decrypted_pos]
            
            if work_char.isupper():
                decrypted_char = decrypted_char.upper()
            
            decrypted.append(decrypted_char)
            key_index += 1
        else:
            decrypted.append(char)
    
    return ''.join(decrypted)

result = vigenere_decrypt(ciphertext, full_key.replace(' ', ''))
print(f"\nПроверка с этим ключом: {result}")
