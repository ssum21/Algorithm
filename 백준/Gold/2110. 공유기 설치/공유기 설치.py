import sys

input = sys.stdin.readline

n, c = map(int, input().split())

a= []
for i in range(n):
    a.append(int(input()))

a.sort()

left, right = 1, a[-1] - a[0]
result = 0

while left <= right:
    mid = (left + right) // 2 # 총 개수
    prev = 0
    count = 1
    for i in range(1, len(a)):
        if(a[i]-a[prev] >= mid):
            count += 1
            prev = i
    if count >= c:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)