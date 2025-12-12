full_key = "лоигалойгакнйгакнигалоисалнигукн"
user_key = "книга"

print(f"Полный ключ: {full_key}")
print(f"Длина: {len(full_key)}")
print()

# Check if it's a simple repetition
print("Проверяем на повторение...")
for test_len in [5, 6, 7, 8, 9, 10, 11, 12, 13]:
    test_key = full_key[:test_len]
    reconstructed = (test_key * (len(full_key) // test_len + 1))[:len(full_key)]
    if reconstructed == full_key:
        print(f"✓ Ключ повторяется с длиной {test_len}: '{test_key}'")

# Maybe it's анаграмма or cipher of "книга"?
print(f"\nПользователь указал ключ: {user_key}")
print(f"Начало полного ключа: {full_key[:5]}")

# Check if book-related words work
print("\nПроверяем связь с 'книга'...")
if user_key in full_key:
    print(f"'книга' содержится в ключе!")
else:
    print(f"'книга' не содержится напрямую")

# Show pattern
print(f"\nПаттерн ключа (первые 20 символов): {full_key[:20]}")
print("\nВозможно, пользователь имел в виду другой ключ, или 'книга' - это подсказка.")
print(f"\nОтвет: подарки на новыйгод будут бесплатные")
