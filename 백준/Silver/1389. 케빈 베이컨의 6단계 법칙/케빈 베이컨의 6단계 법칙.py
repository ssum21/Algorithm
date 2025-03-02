import sys
import math

input = sys.stdin.readline

n,m = map(int, input().split())
result = [[sys.maxsize]*(n) for i in range(n)]
answer = [[0]*(n) for i in range(n)]

for i in range(m):
    s, e = map(int, input().split())
    result[s-1][e-1] = 1
    result[e-1][s-1] = 1

for i in range(n): # 경유지
    for j in range(n): # 출발지
        for k in range(n): #도착지
            if(result[j][i] !=0 and result[i][k]!=0):
                result[j][k] = min(result[j][i] + result[i][k], result[j][k])

num = sys.maxsize
arr = [0]*(n)
for i in range(n):
    arr[i] = sum(result[i])

for i in range(n):
    if (min(arr) == arr[i]):
        print(i+1)
        break