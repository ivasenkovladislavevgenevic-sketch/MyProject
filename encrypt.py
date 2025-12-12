import math

def encrypt(text, key):
    cipher = ""
    k_len = len(key)
    msg_len = len(text)
    
    rows = int(math.ceil(msg_len / k_len))
    
    padding = rows * k_len - msg_len
    text = text + ' ' * padding
    
    matrix = [text[i: i + k_len] for i in range(0, len(text), k_len)]
    
    key_with_indices = sorted([(k, i) for i, k in enumerate(key)])
    order = [i for k, i in key_with_indices]
    
    for col_idx in order:
        for row in matrix:
            cipher += row[col_idx]
            
    return cipher

text = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
key = "СНЕГ"

encrypted_text = encrypt(text, key)
print(f"Encrypted: {encrypted_text}")
