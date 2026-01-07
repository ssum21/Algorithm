import sys
input = sys.stdin.readline

max_value = sys.maxsize

n, k = map(int, input().split())
value = []
for _ in range(n):
    value.append(int(input()))

dp = [max_value] * (k + 1)
dp[0] = 0

value = sorted(set(value))
for v in value:
    for i in range(v, k + 1):
        if dp[i - v] + 1 < dp[i]:
            dp[i] = dp[i - v] + 1
print(dp[k] if dp[k] != max_value else -1)