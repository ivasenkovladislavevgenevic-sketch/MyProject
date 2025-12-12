def caesar_decrypt(ciphertext, shift):
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
    decrypted = []
    for char in ciphertext:
        work_char = char.replace('ё', 'е').replace('Ё', 'Е')
        
        if work_char.lower() in russian_alphabet:
            char_pos = russian_alphabet.index(work_char.lower())
            decrypted_pos = (char_pos - shift) % len(russian_alphabet)
            decrypted_char = russian_alphabet[decrypted_pos]
            
            if work_char.isupper():
                decrypted_char = decrypted_char.upper()
            
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    
    return ''.join(decrypted)


encrypted_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

print("Пробуем разные сдвиги Цезаря:")
for shift in range(1, 33):
    result = caesar_decrypt(encrypted_text, shift)
    print(f"Сдвиг {shift:2d}: {result}")
