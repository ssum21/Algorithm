from itertools import combinations
import sys
from itertools import permutations
from itertools import product
import math

input = sys.stdin.readline

result = set()
n, m = map(int, input().split())
a = list(map(int,input().split()))
a = sorted(a)
for i in permutations(a, m):
    result.add((i))

result = sorted(result)

for i in result:
    print(*i)