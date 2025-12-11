# ACMP.RU - Zadacha 0002: Summa

## Uslovie

**Zadacha:** Najti summu N chisel.

**Vhod:**
- Pervaya stroka: N (kolichestvo chisel, 1 ≤ N ≤ 10000)
- Sleduyushchie N strok: po odnomu chislu v kazhdoj stroke

**Vyhod:** Summa vseh N chisel

---

## Reshenie 1: Klassicheskoe (LUCHSHEE dlya nachinayushchih)

```python
n = int(input())
total = 0
for i in range(n):
    total += int(input())
print(total)
```

### Obyasnenie:

**Stroka 1:** `n = int(input())`
- Chitaem kolichestvo chisel
- Preobrazuem v int

**Stroka 2:** `total = 0`
- Sozdaem peremennuyu dlya nakopleniya summy
- Nachinalnoe znachenie = 0

**Stroki 3-4:** `for i in range(n):`
- Povtoryaem N raz
- range(n) sozdaet posledovatelnost 0, 1, 2, ..., n-1

**Stroka 4:** `total += int(input())`
- Chitaem sledulyushchee chislo
- Preobrazuem v int
- Dobavlyaem k total
- `total += x` eto sokrashchenie dlya `total = total + x`

**Stroka 5:** `print(total)`
- Vyvodim itogoluyu summu

---

## Reshenie 2: Optimizirovannoe (KOROTKO!)

```python
n = int(input())
print(sum(int(input()) for i in range(n)))
```

### Obyasnenie:

**Chto takoe `sum()`?**
- Vstroenaya funkciya Python
- Skladyvaet vsye elementy

**Chto takoe generator expression?**
```python
(int(input()) for i in range(n))
```
- Eto lenivyj iterator
- Generiruet chisla po odnomu
- Ne sozdaet spisok v pamyati (effektivno!)

**Kak rabotaet:**
1. `range(n)` - povtorjaet n raz
2. `int(input())` - chitaet chislo kazhdyj raz
3. `sum(...)` - skladyvaet vsye

---

## Sravnenie

| Kriterii | Reshenie 1 | Reshenie 2 |
|----------|-----------|-----------|
| Stroki koda | 5 | 2 |
| Chitaemost | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Kratost | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Skorost | O(n) | O(n) |
| Pamyat | O(1) | O(1) |

**Vyvod:** Oba resheniya ravno effektivny. Vybirayte:
- **Reshenie 1** - esli vy nachinayushchij
- **Reshenie 2** - esli znaete Python

---

## Primery

### Primer 1:
**Vvod:**
```
3
5
3
2
```
**Vyvod:** `10`

**Poshagovo:**
- n = 3 (budem chitat 3 chisla)
- total = 0
- Iteraciya 1: total = 0 + 5 = 5
- Iteraciya 2: total = 5 + 3 = 8
- Iteraciya 3: total = 8 + 2 = 10
- Vyvodit: 10

### Primer 2:
**Vvod:**
```
5
10
-5
20
-10
15
```
**Vyvod:** `30`

**Raschot:** 10 + (-5) + 20 + (-10) + 15 = 30

---

## Klyuchevye momenty

1. **Chitat N chisel v cikle**
2. **Ispolzovat nakopitel (total)**
3. **Ne zabyt nachalnoe znachenie 0**
4. **Ili ispolzovat sum() dlya kratosti**

---

## Rasprostranennye oshibki

### Oshibka 1: Popytka prochitat vsyo srazu
```python
# NEPRAVILNO!
numbers = input().split()  # Ne rabotaet - chisla v raznykh strokakh!
```

### Oshibka 2: Zabyli preobrazovat v int
```python
# NEPRAVILNO!
total = 0
for i in range(n):
    total += input()  # Oshibka! input() vozvrashchaet stroku
```

### Oshibka 3: Nepravilnoe nachalnoe znachenie
```python
# NEPRAVILNO!
total = 1  # Dolzhno byt 0!
```

---

## Testirovanie

Vse testy projdeny:
- Test 1: 3 chisla (5, 3, 2) → 10 ✅
- Test 2: Otritsatelnye chisla → Rabotaet ✅
- Test 3: Bolshie chisla → Rabotaet ✅
