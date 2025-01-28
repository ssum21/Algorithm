import sys

input = sys.stdin.readline().rstrip()
arr = []
temp = -500001
n = int(input)

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    arr.append((num, i))

arr=sorted(arr)

for i in range(n):
    temp = max(temp, arr[i][1] - i)

print(temp+1)