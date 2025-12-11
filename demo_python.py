"""
Interaktivnaya demonstraciya resheniya zadachi A+B
"""

print("=" * 60)
print("ACMP.RU - Zadacha 0001: A+B")
print("=" * 60)
print()

# Demonstraciya 1: Pokazyvaem kazhdyj shag
print("📚 DEMONSTRACIYA 1: Poshagovoe vypolnenie")
print("-" * 60)

test_input = "2 3"
print(f"Vvod: {test_input}")
print()

# Shag 1
print("Shag 1: input()")
print(f"  Rezultat: '{test_input}' (tip: {type(test_input).__name__})")
print()

# Shag 2
result_split = test_input.split()
print("Shag 2: split()")
print(f"  Rezultat: {result_split}")
print(f"  Tip elementov: {type(result_split[0]).__name__}")
print()

# Shag 3
print("Shag 3: map(int, ...)")
print(f"  int('{result_split[0]}') → {int(result_split[0])}")
print(f"  int('{result_split[1]}') → {int(result_split[1])}")
print()

# Shag 4
a, b = map(int, result_split)
print("Shag 4: a, b = ...")
print(f"  a = {a} (tip: {type(a).__name__})")
print(f"  b = {b} (tip: {type(b).__name__})")
print()

# Shag 5
result = a + b
print("Shag 5: print(a + b)")
print(f"  Vyichislyaem: {a} + {b} = {result}")
print(f"  Vyvod: {result}")
print()

# Demonstraciya 2: Razlichnye testy
print("=" * 60)
print("📊 DEMONSTRACIYA 2: Testirovanie na raznykh dannyh")
print("-" * 60)

test_cases = [
    ("2 3", "Obychnye chisla"),
    ("-5 10", "Otritsatelnoe + polozhitelnoe"),
    ("-10 -20", "Oba otritsatelnye"),
    ("1000000000 1000000000", "Bolshie chisla"),
    ("0 0", "Nuli"),
    ("2    3", "Mnogo probelov"),
]

for test_input, description in test_cases:
    a, b = map(int, test_input.split())
    result = a + b
    print(f"Test: {description}")
    print(f"  Vvod: '{test_input}'")
    print(f"  Vyvod: {result}")
    print()

# Demonstraciya 3: Chto proishodit s map()
print("=" * 60)
print("🔍 DEMONSTRACIYA 3: Kak rabotaet map()")
print("-" * 60)

string_list = ["2", "3"]
print(f"1. Ishodnyj spisok strok: {string_list}")
print()

map_object = map(int, string_list)
print(f"2. Rezultat map(int, ...): {map_object}")
print(f"   Tip: {type(map_object).__name__}")
print()

# Preobrazuem v spisok dlya prosmotra
int_list = list(map(int, ["2", "3"]))
print(f"3. Esli preobrazovat v spisok: {int_list}")
print(f"   Tip elementov: {type(int_list[0]).__name__}")
print()

# Pokazyvaem raspakovku
a, b = map(int, ["2", "3"])
print(f"4. Pri raspakovke (a, b = ...):")
print(f"   a = {a}, b = {b}")
print()

# Demonstraciya 4: Sravnenie sposobov
print("=" * 60)
print("⚖️  DEMONSTRACIYA 4: Sravnenie raznyh sposobov")
print("-" * 60)

test_input = "2 3"

print("Sposob 1 (LUCHSHIJ):")
print("  a, b = map(int, input().split())")
a, b = map(int, test_input.split())
print(f"  Rezultat: {a + b}")
print(f"  Stroki koda: 2")
print()

print("Sposob 2 (Cherez spisok):")
print("  numbers = list(map(int, input().split()))")
numbers = list(map(int, test_input.split()))
print(f"  Rezultat: {numbers[0] + numbers[1]}")
print(f"  Stroki koda: 2")
print(f"  Lishnij obyekt: {numbers}")
print()

print("Sposob 3 (Po shagam):")
print("  line = input()")
print("  parts = line.split()")
print("  a = int(parts[0])")
print("  b = int(parts[1])")
line = test_input
parts = line.split()
a = int(parts[0])
b = int(parts[1])
print(f"  Rezultat: {a + b}")
print(f"  Stroki koda: 5")
print()

# Demonstraciya 5: Rasprostranennye oshibki
print("=" * 60)
print("⚠️  DEMONSTRACIYA 5: Rasprostranennye oshibki")
print("-" * 60)

print("Oshibka 1: Zabyli preobrazovat v int")
a, b = "2", "3"
print(f"  a, b = '2', '3' (stroki)")
print(f"  a + b = '{a + b}' (konkatenaciya!) ❌")
a, b = 2, 3
print(f"  a, b = 2, 3 (chisla)")
print(f"  a + b = {a + b} ✅")
print()

print("Oshibka 2: Nevernyi vyvod")
a, b = 2, 3
print(f"  print(a, b) → vyvedet '{a} {b}' ❌")
print(f"  print(a + b) → vyvedet '{a + b}' ✅")
print()

print("Oshibka 3: Vyvod stroki")
print(f"  print('a + b') → vyvedet 'a + b' ❌")
print(f"  print(a + b) → vyvedet '{a + b}' ✅")
print()

# Zaklyuchenie
print("=" * 60)
print("🎯 ITOGOVOE RESHENIE")
print("=" * 60)
print()
print("a, b = map(int, input().split())")
print("print(a + b)")
print()
print("✅ Kratko")
print("✅ Effektivno") 
print("✅ Nadezhno")
print("✅ Pythonic")
print()
print("Gotovo k otpravke na acmp.ru! 🚀")
print("=" * 60)
