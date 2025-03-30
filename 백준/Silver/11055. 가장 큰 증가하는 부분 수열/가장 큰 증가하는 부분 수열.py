import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
DP = [lst[i] for i in range(n)]

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            DP[i] = max(DP[i], DP[j]+lst[i])

print(max(DP))