# -*- coding: utf-8 -*-
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ciphertext = "ъьмгрхц цг ншпдмгшс йцдюа йцсъшихаёт"
key = "книга"

def decrypt(text, key):
    res = []
    key_idx = 0
    key_indices = [alphabet.index(k) for k in key]
    for char in text:
        if char in alphabet:
            c_idx = alphabet.index(char)
            k_idx_val = key_indices[key_idx % len(key)]
            p_idx = (c_idx - k_idx_val) % len(alphabet)
            res.append(alphabet[p_idx])
            key_idx += 1
        else:
            res.append(char)
    return "".join(res)

print(decrypt(ciphertext, key))
