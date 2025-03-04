import sys
input = sys.stdin.readline

n = int(input())

D = [[0 for i in range(10)] for i in range(n+1)]

for i in range(1, 10):
    D[0][i] = 1

for j in range(1, n):
    for k in range(10):
        if k==0:
            D[j][k] = D[j-1][k+1]
        elif k==9:
            D[j][k] = D[j-1][k-1]
        else:
            D[j][k] = (D[j-1][k-1] + D[j-1][k+1]) %1000000000

print(sum(D[n-1])%1000000000)
