# -*- coding: utf-8 -*-
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
cipher = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
key = "книга"
plain = ""
key_idx = 0
for char in cipher.lower():
    if char in alphabet:
        c_idx = alphabet.index(char)
        k_idx = alphabet.index(key[key_idx % len(key)])
        p_idx = (c_idx - k_idx) % len(alphabet)
        plain += alphabet[p_idx]
        key_idx += 1
    else:
        plain += char
print(plain)
