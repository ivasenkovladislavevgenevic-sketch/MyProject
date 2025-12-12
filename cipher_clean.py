def encrypt_transposition(key, message):
    n = len(key)
    columns = [''] * n
    for i, char in enumerate(message):
        col = i % n
        columns[col] += char
    key_indices = sorted(range(n), key=lambda k: key[k])
    result = ''
    for i in key_indices:
        result += columns[i]
    return result

if __name__ == "__main__":
    msg = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
    key = "SECRET" 
    print(encrypt_transposition(key, msg))
