import math

def columnar_transposition(text, key):
    text = text.replace(" ", "")
    num_cols = key
    num_rows = math.ceil(len(text) / num_cols)
    num_padding = num_rows * num_cols - len(text)
    text += "_" * num_padding
    
    matrix = []
    index = 0
    for row in range(num_rows):
        row_data = []
        for col in range(num_cols):
            if index < len(text):
                row_data.append(text[index])
                index += 1
        matrix.append(row_data)
    
    encrypted = ""
    for col in range(num_cols):
        for row in range(num_rows):
            if row < len(matrix) and col < len(matrix[row]):
                encrypted += matrix[row][col]
    
    return encrypted

def rail_fence(text, rails):
    text = text.replace(" ", "")
    if rails <= 1:
        return text
    
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in text:
        fence[rail].append(char)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    
    encrypted = ""
    for rail_chars in fence:
        encrypted += "".join(rail_chars)
    
    return encrypted

original = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"

print("=" * 70)
print("TRANSPOSITION CIPHER ENCRYPTION")
print("=" * 70)
print(f"\nOriginal text:\n{original}")
print(f"\nLength (no spaces): {len(original.replace(' ', ''))}")

print("\n" + "-" * 70)
print("METHOD 1: COLUMNAR TRANSPOSITION (key=7)")
print("-" * 70)
result1 = columnar_transposition(original, 7)
print(f"Encrypted: {result1}")

print("\n" + "-" * 70)
print("METHOD 2: COLUMNAR TRANSPOSITION (key=9)")
print("-" * 70)
result2 = columnar_transposition(original, 9)
print(f"Encrypted: {result2}")

print("\n" + "-" * 70)
print("METHOD 3: RAIL FENCE (rails=3)")
print("-" * 70)
result3 = rail_fence(original, 3)
print(f"Encrypted: {result3}")

print("\n" + "-" * 70)
print("METHOD 4: RAIL FENCE (rails=5)")
print("-" * 70)
result4 = rail_fence(original, 5)
print(f"Encrypted: {result4}")

print("\n" + "=" * 70)
