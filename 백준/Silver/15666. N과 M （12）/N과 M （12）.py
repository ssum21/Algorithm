from itertools import combinations_with_replacement
import sys
from itertools import permutations
from itertools import product
import math

input = sys.stdin.readline

result = set()
n, m = map(int, input().split())
a = list(map(int,input().split()))
a = sorted(a)
for i in combinations_with_replacement(a, m):
    result.add((i))

result = sorted(result)

for i in result:
    print(*i)