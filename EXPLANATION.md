# ACMP.RU - Zadacha 0001: A+B

## Uslovie zadachi

Dana klassicheskaya zadacha "A+B" - pervaya zadacha na sajte acmp.ru.

**Vhod:** Dva celyh chisla A i B cherez probel (-10^9 <= A, B <= 10^9)
**Vyhod:** Odno chislo - summa A i B

### Primery

**Primer 1:**
- Vhod: `2 3`
- Vyhod: `5`

**Primer 2:**
- Vhod: `-5 10`
- Vyhod: `5`

**Primer 3:**
- Vhod: `1000000000 1000000000`
- Vyhod: `2000000000`

## Reshenie na Python

```python
# Schityvaem dva chisla
a, b = map(int, input().split())

# Vyvodim ih summu
print(a + b)
```

### Ob'yasnenie Python-resheniya:

1. **input()** - schityvaet stroku s vvoda
2. **.split()** - razbivaet stroku po probelam, poluchaem spisok iz dvuh strok
3. **map(int, ...)** - preobrazuet kazhdyj element spiska v celoe chislo
4. **a, b = ...** - raspakovyvaem dva chisla v peremennye a i b
5. **print(a + b)** - skladyvaem i vyvodim rezultat

**Slozhnost:** O(1) po vremeni i pamyati

## Reshenie na C++

```cpp
#include <iostream>
using namespace std;

int main() {
    long long a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}
```

### Ob'yasnenie C++-resheniya:

1. **#include <iostream>** - podklyuchaem biblioteku vvoda-vyvoda
2. **long long** - ispolzuem 64-bitnyj tip (vmeshaet znacheniya do 10^18)
3. **cin >> a >> b** - schityvaem dva chisla
4. **cout << a + b << endl** - vyvodim summu s perevodom stroki
5. **return 0** - zavershenie programmy s kodom uspeha

**Pochemu long long?** 
- Maksimalnye znacheniya A i B mogut byt do 10^9
- Ih summa mozhet byt do 2*10^9, chto vmeshaetsya v long long
- Tip int na mnogih sistemah vmeshaet tolko do ~2*10^9

**Slozhnost:** O(1) po vremeni i pamyati

## Vazhnye momenty

1. **Ogranicheniya:**
   - Chisla mogut byt otritsatelnymi
   - Nuzhno uchityvat bolshie znacheniya (do 10^9)

2. **Rasprostranennye oshibki:**
   - Ispolzovanie int vmesto long long v C++
   - Zabyvanie schitat oba chisla
   - Nevernoe chtenie vvoda

3. **Optimizaciya:**
   - Zadacha uzhe maksimalno optimizirована
   - Nelzya sdelat bystree chem O(1)

## Testirovanie

Zapustit Python:
```bash
python3 acmp_0001.py
```

Skompilirovat i zapustit C++:
```bash
g++ -o acmp_0001 acmp_0001.cpp
./acmp_0001
```

Testirovat s fajlom:
```bash
python3 acmp_0001.py < test_input.txt
./acmp_0001 < test_input.txt
```
