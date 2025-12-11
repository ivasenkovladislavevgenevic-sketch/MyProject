# ACMP.RU - Zadacha 0001: A+B (Python)

## Uslovie zadachi

**Zadacha:** Dany dva celyh chisla A i B. Najti ih summu.

**Vhod:** Dva celyh chisla A i B cherez probel (-10^9 ≤ A, B ≤ 10^9)

**Vyhod:** Odno chislo - summa A i B

---

## Reshenie

```python
a, b = map(int, input().split())
print(a + b)
```

**Eto samoe prostoe, korrektnoe i effektivnoe reshenie!**

---

## Poshagovyj razbor koda

### Stroka 1: `a, b = map(int, input().split())`

Eto samaya vazhnaya stroka! Razberem ee sprava nalevo:

#### 1️⃣ `input()` - Chtenie s konsoli

```python
input()
```

**Chto delaet:**
- Ostanavlivaet vypolnenie programmy
- Zhdet, poka polzovatel vvedet danye i nazhmot Enter
- Vozvrashchaet STROKU (tip: str)

**Primer:**
```
Polzovatel vvodit: 2 3 [Enter]
input() vozvrashchaet: "2 3"
```

#### 2️⃣ `.split()` - Razdelenie stroki

```python
"2 3".split()
```

**Chto delaet:**
- Razbivaet stroku po PROBELAM (po umolchaniyu)
- Udalaet VSYE lishniye probely (v nachale, v konce, mezhdu slovami)
- Vozvrashchaet SPISOK strok

**Primery:**

```python
"2 3".split()          # → ["2", "3"]
"2    3".split()       # → ["2", "3"]  (mnogo probelov)
"  2 3  ".split()      # → ["2", "3"]  (probely v nachale/konce)
"-5 10".split()        # → ["-5", "10"]
```

**Vazhno:** Vse elementy spiska - eto STROKI, ne chisla!

#### 3️⃣ `map(int, ...)` - Preobrazovanie v chisla

```python
map(int, ["2", "3"])
```

**Chto delaet:**
- Primenyaet funkciyu `int()` k KAZHDOMU elementu spiska
- `int()` preobrazuet STROKU v CELOE CHISLO
- Vozvrashchaet iterator (lenivyj obekt)

**Vizualizaciya:**

```
["2", "3"]
   ↓    ↓
int("2") int("3")
   ↓    ↓
   2    3
```

**Pochemu ne spisok?**
```python
# map() vozvrashchaet iterator, ne spisok
result = map(int, ["2", "3"])
print(result)  # <map object at 0x...>

# Chtoby poluchiyt spisok:
result = list(map(int, ["2", "3"]))
print(result)  # [2, 3]

# No nam ne nuzhen spisok, my srazu raspakovyvaem!
```

#### 4️⃣ `a, b = ...` - Raspakovka (Unpacking)

```python
a, b = map(int, ["2", "3"])
```

**Chto delaet:**
- Beriot PERVOE znachenie iz iteratora → sohranyaet v `a`
- Beriot VTOROE znachenie iz iteratora → sohranyaet v `b`
- Oba znacheniya teper - celyye chisla (int)

**Vizualizaciya:**

```
map(int, ["2", "3"])
       ↓        ↓
      2        3
      ↓        ↓
    a = 2    b = 3
```

**Vazhno:** Kolichestvo peremennyh DOLZHNO sovpadat s kolichestvom elementov!

```python
# Pravilno
a, b = [1, 2]           # OK

# Oshibka!
a, b = [1, 2, 3]        # ValueError: too many values to unpack
a, b, c = [1, 2]        # ValueError: not enough values to unpack
```

### Stroka 2: `print(a + b)`

```python
print(a + b)
```

**Chto delaet:**
1. **Snacha vyichislyaetsya vyrazhenie:** `a + b`
   - Esli a=2 i b=3, to: 2 + 3 = 5

2. **Potom vyvodit rezultat:** `print(5)`
   - Vyvodit chislo 5 v konsol
   - Avtomaticheski dobavlyaet perevod stroki (\n) v konce

**Vazhno:** Ne putayte!

```python
# Pravilno
print(a + b)        # Vyvodit: 5

# Nepravilno!
print(a, b)         # Vyvodit: 2 3 (s probelom)
print("a + b")      # Vyvodit: a + b (stroku!)
print(a, "+", b)    # Vyvodit: 2 + 3
```

---

## Polnyj primer vypolneniya

Davajte poprobuem vypolnit programmu poshagovo:

```
VVOD POLZOVATELYA: 2 3 [Enter]

Shag 1: input()
  Rezultat: "2 3" (stroka)

Shag 2: "2 3".split()
  Rezultat: ["2", "3"] (spisok strok)

Shag 3: map(int, ["2", "3"])
  Primenyaem int() k kazhdomu elementu:
    int("2") → 2
    int("3") → 3
  Rezultat: iterator s [2, 3]

Shag 4: a, b = ...
  a = 2 (int)
  b = 3 (int)

Shag 5: print(a + b)
  Vyichislyaem: 2 + 3 = 5
  Vyvodim: 5

VYVOD: 5
```

---

## Pochemu eto reshenie MAKSIMALNO PRAVILNOE?

### ✅ 1. Effektivnost

**Vremya:** O(1) - konstantnoe
- Chitaem vvod: O(1)
- Skladyvaem dva chisla: O(1)

**Pamyat:** O(1) - konstantnaya
- Vsego 2 peremennye

### ✅ 2. Nadezhnost

**Avtomaticheskaya rabota s bolshimi chislami:**

```python
# Python AVTOMATICHESKI rabotaet s lyubymi chislami!
a, b = 1000000000, 1000000000
print(a + b)  # 2000000000 - OK!

a, b = 10**100, 10**100
print(a + b)  # 2 * 10^100 - TOZHE OK!
```

Python ne imeet ogranichenij na razmer celyx chisel!

### ✅ 3. Prostota

- Vsego 2 stroki koda
- Legko chitat i ponimat
- Net lishnikh peremennyh

### ✅ 4. Universalnost

```python
# Rabotaet so vsemi sluchayami:

# Polozhitelnye chisla
"2 3" → 5

# Otritsatelnye chisla
"-5 10" → 5
"-10 -20" → -30

# Bolshie chisla
"1000000000 1000000000" → 2000000000

# Mnogo probelov
"2    3" → 5

# Probely v nachale/konce
"  2 3  " → 5
```

---

## Alternativnye sposoby resheniya

### Sposob 1: Nash (Luchshij!)

```python
a, b = map(int, input().split())
print(a + b)
```

**Plyusy:** Kratko, effektivno, pythonic
**Minusy:** Net

---

### Sposob 2: Cherez spisok

```python
numbers = list(map(int, input().split()))
print(numbers[0] + numbers[1])
```

**Plyusy:** Ponyatno novichkam
**Minusy:** 
- Dlinnee
- Sozdaet lishnij spisok
- Menee pythonic
- Ispolzuet bolshe pamyati

---

### Sposob 3: Po shagam

```python
line = input()
parts = line.split()
a = int(parts[0])
b = int(parts[1])
print(a + b)
```

**Plyusy:** Ochenb ponyatno novichkam
**Minusy:**
- Slishkom mnogo strok (5 vmesto 2)
- Mnogo promezhutochnyh peremennyh
- Zanimaet bolshe pamyati

---

### Sposob 4: List comprehension

```python
a, b = [int(x) for x in input().split()]
print(a + b)
```

**Plyusy:** Tozhe pythonic
**Minusy:**
- Sozdaet spisok (lishnee)
- map() effektivnee (ne sozdaet spisok)

---

### Sposob 5: Dva input()

```python
a = int(input())
b = int(input())
print(a + b)
```

**Plyusy:** Ochenb prosto
**Minusy:**
- ❌ NE PODHODIT dlya etoj zadachi!
- Trebuet DVUH strok vvoda:
  ```
  2
  3
  ```
- A v zadache chisla v ODNOJ stroke: `2 3`

---

## Rasprostranennye oshibki

### ❌ Oshibka 1: Zabyli split()

```python
a, b = map(int, input())  # OSHIBKA!
```

**Problema:**
- `input()` vozvrashchaet stroku "2 3"
- `map(int, "2 3")` primenit int() k KAZHDOMU SIMVOLU
- int("2") → OK
- int(" ") → ValueError!

**Ispravlenie:**
```python
a, b = map(int, input().split())  # PRAVILNO!
```

---

### ❌ Oshibka 2: Nevernyi vyvod

```python
a, b = map(int, input().split())
print(a, b)  # Vyvedet: 2 3 (ne 5!)
```

**Ispravlenie:**
```python
print(a + b)  # Vyvedet: 5
```

---

### ❌ Oshibka 3: Vyvod stroki

```python
a, b = map(int, input().split())
print("a + b")  # Vyvedet: a + b (ne 5!)
```

**Ispravlenie:**
```python
print(a + b)  # BEZ kavy chek!
```

---

### ❌ Oshibka 4: Ispolzovanie +

```python
a, b = input().split()  # Zabyli map(int, ...)
print(a + b)  # Vyvedet: 23 (slozhenie strok!)
```

**Problema:**
- `a = "2"` i `b = "3"` (stroki)
- `"2" + "3"` = `"23"` (konkatenaciya strok)

**Ispravlenie:**
```python
a, b = map(int, input().split())  # Preobrazuem v int!
print(a + b)  # 5
```

---

## Testirovanie

Davajte protestiruem nashe reshenie:

```python
# Test 1: Obychnye chisla
Vvod: 2 3
Ozhidaemyj vyvod: 5
Rezultat: ✅

# Test 2: Otritsatelnye chisla
Vvod: -5 10
Ozhidaemyj vyvod: 5
Rezultat: ✅

# Test 3: Oba otritsatelnye
Vvod: -10 -20
Ozhidaemyj vyvod: -30
Rezultat: ✅

# Test 4: Bolshie chisla
Vvod: 1000000000 1000000000
Ozhidaemyj vyvod: 2000000000
Rezultat: ✅

# Test 5: Nol
Vvod: 0 0
Ozhidaemyj vyvod: 0
Rezultat: ✅

# Test 6: Mnogo probelov
Vvod: 2    3
Ozhidaemyj vyvod: 5
Rezultat: ✅
```

---

## Zaklyuchenie

### Itogovoe reshenie:

```python
a, b = map(int, input().split())
print(a + b)
```

### Pochemu eto luchshee reshenie?

1. ✅ **Kratko** - vsego 2 stroki
2. ✅ **Effektivno** - O(1) po vremeni i pamyati
3. ✅ **Nadezhno** - rabotaet so vsemi sluchayami
4. ✅ **Pythonic** - ispolzuet idiomy Python
5. ✅ **Universalno** - ne trebuet dopolnitelnyh bibliotek

### Klyuchevye momenty:

- `input()` - chitaet STROKU
- `.split()` - razbivaet po probelam
- `map(int, ...)` - preobrazuet v chisla
- `a, b = ...` - raspakovka znachenij
- `print(a + b)` - vyvod summy

**Eto reshenie gotovo k otpravke na acmp.ru!** 🎉
