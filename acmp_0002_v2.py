# ACMP.RU - Task 0002: Summa ot N do M
# Find sum from N to M (inclusive)

n, m = map(int, input().split())
total = (n + m) * (m - n + 1) // 2
print(total)
