from itertools import combinations
import sys
from math import factorial
from math import comb

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
k = int(input())
total = sum(a)
arrtot = 0
for i in a:
    arrtot += comb(i, k)

print(arrtot / (comb(total, k)))
