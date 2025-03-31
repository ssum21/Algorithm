import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp_table = [1 for i in range(n+1)]
prev = [-1 for i in range(n+1)]

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j] and dp_table[i] < dp_table[j] + 1:
            dp_table[i] = dp_table[j] + 1
            prev[i] = j

k = max(dp_table)
idx = dp_table.index(k)
result = []

while idx!=-1:
    result.append(lst[idx])
    idx = prev[idx]


result.reverse()

print(k)
print(*result)