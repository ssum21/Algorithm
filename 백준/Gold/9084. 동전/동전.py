import sys
from collections import deque, defaultdict
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
inf = sys.maxsize

T = int(input())

for i in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    goal = int(input())
    dp = [0 for _ in range(goal+1)]
    dp[0] = 1
    for coin in coins:
        for j in range(coin, goal+1):
            dp[j] += dp[j-coin]
    
    print(dp[goal])