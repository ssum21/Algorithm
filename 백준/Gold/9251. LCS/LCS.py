import sys

input = sys.stdin.readline

N = list(map(str, input().strip()))
M = list(map(str, input().strip()))

len_N = len(N)
len_M = len(M)

arr = [[0 for i in range(len_N+1)] for j in range(len_M+1)]

tot = 0
i=0
j=0

for j in range(1, len_M+1):
    for i in range(1, len_N+1):
        if(N[i-1] == M[j-1]):
            arr[j][i] = arr[j-1][i-1] + 1
        else:
            arr[j][i] = max(arr[j][i-1], arr[j-1][i])

print(arr[len_M][len_N])