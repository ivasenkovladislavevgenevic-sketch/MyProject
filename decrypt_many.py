def vigenere_decrypt(ciphertext, key):
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
    decrypted = []
    key_index = 0
    
    for char in ciphertext:
        work_char = char.replace('ё', 'е').replace('Ё', 'Е')
        
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


encrypted_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

test_keys = [
    "книга", "книжка", "роман", "текст", "слово", "буква",
    "новыйгод", "подарок", "праздник", "зима", "год",
    "логика", "ключ", "шифр", "код"
]

print("Тестируем различные ключи:")
print()

for test_key in test_keys:
    result = vigenere_decrypt(encrypted_text, test_key)
    # Check if result contains readable Russian words
    readable_words = ["подарки", "новый", "год", "будут", "бесплатные", "на"]
    score = sum(1 for word in readable_words if word in result.lower())
    
    marker = " <<<" if score >= 2 else ""
    print(f"Ключ '{test_key:12s}': {result}{marker}")
