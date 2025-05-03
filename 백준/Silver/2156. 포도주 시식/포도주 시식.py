import sys

input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

li_sum = [0 for _ in range(n)]

if(n>=3):
    li_sum[0] = arr[0]
    li_sum[1] = arr[0]+arr[1]
    li_sum[2] = max(arr[0]+arr[1] , arr[1]+arr[2], arr[0]+arr[2])
    for i in range(3, n):
        li_sum[i] = max(li_sum[i-2]+arr[i], li_sum[i-1], li_sum[i-3]+arr[i-1]+arr[i])
    print(li_sum[n-1])
else:
    print(sum(arr))