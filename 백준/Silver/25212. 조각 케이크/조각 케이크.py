import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
total = 0

translate_arr = [0] * n

for i in range(n):
    translate_arr[i] = 1 / arr[i]

for i in range(1, n+1):
    for j in combinations(translate_arr, i):
        k = sum(j)
        if(k>=0.99 and k<=1.01):
            total+=1

print(total)