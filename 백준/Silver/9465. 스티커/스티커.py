import sys
import math

input = sys.stdin.readline

T = int(input().strip()) # 테스트 케이스 개수
for i in range(T):
    arr = [] # 스티커 가중치
    total = 0
    n = int(input().strip()) # 가로 행의 크기
    arr.append(list(map(int,input().split())))
    arr.append(list(map(int,input().split())))
    dp = [[0]*3 for i in range(n)]
    dp[0][0] = 0
    dp[0][1] = arr[0][0]
    dp[0][2] = arr[1][0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + arr[0][i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + arr[1][i]
    print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))