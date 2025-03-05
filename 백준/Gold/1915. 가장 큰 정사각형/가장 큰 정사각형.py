import sys

input = sys.stdin.readline

m, n = map(int, input().split())
arr = []
detect = False
for i in range(m):
    arr.append(list(map(int, input().rstrip())))

for x in range(1, m):
    for y in range(1, n):
        if(arr[x-1][y-1] and arr[x][y-1] and arr[x-1][y] and arr[x][y]):
            arr[x][y] = min(arr[x-1][y-1], arr[x][y-1], arr[x-1][y])  + 1
k=max(map(max, arr))

if(k==0):
    print(k)
else:
    print(k*k)