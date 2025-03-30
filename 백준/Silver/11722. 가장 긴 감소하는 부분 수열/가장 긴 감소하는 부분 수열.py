import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n-1, -1 ,-1):
    for j in range(n-1, i-1, -1):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))