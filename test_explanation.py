# Demonstracija raboty input().split()

print("=== Primer 1: Normalnij vvod ===")
# Simuliruem: "2 3"
test_input = "2 3"
parts = test_input.split()
print(f"Stroka: '{test_input}'")
print(f"Posle split(): {parts}")
print(f"Tip elementov: {type(parts[0])}")

a, b = map(int, parts)
print(f"Posle map(int, ...): a={a}, b={b}")
print(f"Tip chisel: {type(a)}")
print(f"Summa: {a + b}")

print("\n=== Primer 2: Mnogo probelov ===")
test_input2 = "2    3"
parts2 = test_input2.split()
print(f"Stroka: '{test_input2}'")
print(f"Posle split(): {parts2}")
a2, b2 = map(int, parts2)
print(f"Rezultat: {a2 + b2}")

print("\n=== Primer 3: Otritsatelnye chisla ===")
test_input3 = "-5 10"
parts3 = test_input3.split()
a3, b3 = map(int, parts3)
print(f"Vvod: '{test_input3}'")
print(f"Rezultat: {a3} + {b3} = {a3 + b3}")

print("\n=== Primer 4: Bolshie chisla ===")
test_input4 = "1000000000 1000000000"
a4, b4 = map(int, test_input4.split())
print(f"Vvod: '{test_input4}'")
print(f"Rezultat: {a4 + b4}")
print(f"Python legko obrabatvaet bolshie chisla!")
