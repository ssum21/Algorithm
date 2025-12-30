import sys
input = sys.stdin.readline

N, D = map(int, input().split())

shortcuts = [[] for _ in range(D + 1)]

for _ in range(N):
    s, e, dist = map(int, input().split())
    # 도착이 D를 넘어가면 쓸모 없음
    if e > D:
        continue
    # 지름길이 이득이 없으면(그냥 도로보다 길거나 같으면) 쓸모 없음
    if dist >= e - s:
        continue
    shortcuts[s].append((e, dist))

dp = [10**9] * (D + 1)
dp[0] = 0

for i in range(D + 1):
    # 일반 도로로 한 칸 전진
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)

    # i에서 시작하는 지름길 반영
    for e, dist in shortcuts[i]:
        dp[e] = min(dp[e], dp[i] + dist)

print(dp[D])
