def columnar_transposition(text, key):
    text_clean = text.replace(" ", "")
    num_cols = key
    num_rows = (len(text_clean) + num_cols - 1) // num_cols
    padding = num_rows * num_cols - len(text_clean)
    padded = text_clean + 'X' * padding
    
    grid = []
    for i in range(num_rows):
        row = padded[i * num_cols:(i + 1) * num_cols]
        grid.append(list(row))
    
    result = ""
    for col in range(num_cols):
        for row in range(num_rows):
            result += grid[row][col]
    
    return result

text = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
print("Original text:")
print(text)
print("\nEncrypted (Columnar Transposition, key=5):")
print(columnar_transposition(text, 5))
print("\nEncrypted (Columnar Transposition, key=7):")
print(columnar_transposition(text, 7))
