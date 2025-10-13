import sys

input = sys.stdin.readline

result = 0
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(n-1, 0, -1):
    while(arr[i]<=arr[i-1]):
        result+=1
        arr[i-1]-=1

print(result)