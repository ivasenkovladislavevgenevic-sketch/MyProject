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


ciphertext = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

# Try more key variations
import itertools

# The base key seems to be around "книга" or "кнйга"
# Let's try systematic substitutions
base_patterns = [
    "книга",
    "кнйга",
    "лнйга",
    "лнига",
    "лниаа"
]

print("Ищем правильный ключ:")
print()

best_results = []

for key in base_patterns:
    result = vigenere_decrypt(ciphertext, key)
    # Count how many common Russian words appear
    common_words = ["подарки", "на", "новый", "год", "новыйгод", "будут", "бесплатные"]
    score = sum(1 for word in common_words if word in result.lower())
    
    if score > 0:
        best_results.append((score, key, result))
        print(f"✓ Ключ '{key}' (совпадений: {score}): {result}")

print("\n" + "="*60)
print("Лучший результат:")
if best_results:
    best_results.sort(reverse=True)
    score, key, result = best_results[0]
    print(f"Ключ: {key}")
    print(f"Результат: {result}")
