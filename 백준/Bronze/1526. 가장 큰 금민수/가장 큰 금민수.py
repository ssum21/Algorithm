from itertools import product

n = int(input())
result = 0

for i in range(1, len(str(n)) + 1):
    for comb in product(['4', '7'], repeat=i):
        num = int(''.join(comb))
        if num <= n:
            result = max(result, num)

print(result)
