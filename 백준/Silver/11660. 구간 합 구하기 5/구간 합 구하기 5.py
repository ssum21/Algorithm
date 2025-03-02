import sys

input = sys.stdin.readline

n, m = map(int,input().split())

arr = []
arr_sum = [[0]*1025 for i in range(1025)]

for i in range(n):
    arr.append(list(map(int, input().split())))

for j in range(1, n+1):
    for k in range(1, n+1):
        arr_sum[j][k] = arr_sum[j][k-1] + arr_sum[j-1][k] - arr_sum[j-1][k-1] + arr[j-1][k-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    result = arr_sum[x2][y2] + arr_sum[x1-1][y1-1] - arr_sum[x1-1][y2] - arr_sum[x2][y1-1]
    print(result)