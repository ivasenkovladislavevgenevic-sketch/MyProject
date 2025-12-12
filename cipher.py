import math

plaintext = "НАСТУПЛЕНИЕ НА ФРОНТАХ НА НОВОГОДНИХ ПРАЗДНИКАХ НЕ БУДЕТ"
text = plaintext.replace(" ", "")

print("ИСХОДНЫЙ ТЕКСТ:", plaintext)
print("БЕЗ ПРОБЕЛОВ:", text)
print("ДЛИНА:", len(text), "символов")
print()

# Колонная транспозиция с ключом 5
key = 5
num_rows = math.ceil(len(text) / key)
padding = key * num_rows - len(text)
text_padded = text + "Х" * padding

print("=" * 50)
print("КОЛОННАЯ ТРАНСПОЗИЦИЯ (5 колонок)")
print("=" * 50)
print()
print("Матрица заполнения (по строкам):")
print("-" * 20)

matrix = []
for i in range(num_rows):
    row = text_padded[i * key:(i + 1) * key]
    matrix.append(row)
    print(row)

print("-" * 20)
print()

# Читаем по колонкам
cipher = ""
for col in range(key):
    for row in matrix:
        cipher += row[col]

print("ЗАШИФРОВАННЫЙ ТЕКСТ (читаем по колонкам):")
print(cipher)
print()

# Rail Fence
print("=" * 50)
print("RAIL FENCE (3 рельса)")
print("=" * 50)
text = plaintext.replace(" ", "")
rails = 3
fence = [[] for _ in range(rails)]
rail = 0
direction = 1

for char in text:
    fence[rail].append(char)
    rail += direction
    if rail == 0 or rail == rails - 1:
        direction *= -1

print()
for i, row in enumerate(fence):
    print(f"Рельс {i+1}: {''.join(row)}")

cipher2 = "".join("".join(row) for row in fence)
print()
print("ЗАШИФРОВАННЫЙ ТЕКСТ:")
print(cipher2)
