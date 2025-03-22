import sys
from itertools import combinations

input = sys.stdin.readline

arr = []

for i in range(9):
    arr.append(int(input()))

for i in combinations(arr, 7):
    if(sum(i)==100):
        k = list(i)
        break

k.sort()

for i in k:
    print(i)