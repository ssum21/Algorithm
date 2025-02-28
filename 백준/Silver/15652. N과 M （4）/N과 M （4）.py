import sys
import math
from itertools import combinations_with_replacement

N, M = map(int, input().split())

a=[]

for i in range(1, N+1):
    a.append(i)

for i in combinations_with_replacement(a, M):
    print(*i)