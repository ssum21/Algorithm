import sys
import math
from itertools import permutations

N, M = map(int, input().split())
a=list(map(int, input().split()))

a.sort()

for i in permutations(a, M):
    print(*i)