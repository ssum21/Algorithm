import sys

input = sys.stdin.readline

N, M = map(int, input().split())

a = []
for i in range(N):
    a.append(int(input()))

low, high = 0, max(a)*M
result = high
while low<=high:
    mid = (low+high)//2
    value = 0
    for time in a:
        value += (mid // time)
    
    if value >= M:
        result = mid
        high = mid - 1
    else:
        low = mid + 1

print(result)