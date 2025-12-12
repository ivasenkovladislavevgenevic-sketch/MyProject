#!/usr/bin/env python3
encrypted_text = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"

def decrypt_vigenere(encrypted, key_text):
    encrypted_clean = encrypted.replace(' ', '').lower()
    key_clean = ''.join([c for c in key_text.lower() if c.isalpha()])
    
    if not key_clean:
        return None
    
    decrypted = []
    key_index = 0
    
    for char in encrypted_clean:
        if ord('а') <= ord(char) <= ord('я'):
            enc_pos = ord(char) - ord('а')
            key_char = key_clean[key_index % len(key_clean)]
            key_pos = ord(key_char) - ord('а')
            
            dec_pos = (enc_pos - key_pos) % 33
            decrypted_char = chr(ord('а') + dec_pos)
            decrypted.append(decrypted_char)
            
            key_index += 1
    
    result = ''.join(decrypted)
    spaced_result = []
    enc_idx = 0
    for char in encrypted:
        if char == ' ':
            spaced_result.append(' ')
        else:
            if enc_idx < len(result):
                spaced_result.append(result[enc_idx])
                enc_idx += 1
    
    if enc_idx < len(result):
        spaced_result.extend(result[enc_idx:])
    
    return ''.join(spaced_result)

def try_caesar_shift(text, shift):
    result = []
    for char in text.lower():
        if ord('а') <= ord(char) <= ord('я'):
            pos = ord(char) - ord('а')
            new_pos = (pos - shift) % 33
            result.append(chr(ord('а') + new_pos))
        elif char == ' ':
            result.append(' ')
        else:
            result.append(char)
    return ''.join(result)

print("Зашифрованный текст:", encrypted_text)
print("\nПопытка 1: Простой сдвиг (Цезарь)")
for shift in range(1, 10):
    decrypted = try_caesar_shift(encrypted_text, shift)
    print(f"Сдвиг {shift}: {decrypted}")

print("\nПопытка 2: Виженер с известными книгами")
possible_books = {
    "Война и мир": "Ну что ж князь Генуя и Лукка стали не более как поместьями фамилии Бонапарте",
    "Преступление и наказание": "В начале июля в чрезвычайно жаркое время под вечер один молодой человек вышел из своей каморки",
    "Евгений Онегин": "Мой дядя самых честных правил когда не в шутку занемог он уважать себя заставил и лучше выдумать не мог",
    "Мастер и Маргарита": "Однажды весною в час небывало жаркого заката в Москве на Патриарших прудах появились два гражданина",
}

for book_name, book_text in possible_books.items():
    decrypted = decrypt_vigenere(encrypted_text, book_text)
    if decrypted:
        print(f"\n{book_name}:")
        print(f"  {decrypted}")
