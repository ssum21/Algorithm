import math
import sys

n = int(input())
k = int(input())

start = 1
end = k
result = 0
while start <= end:
    mid = int((start + end)/2)
    tot = 0
    for i in range(1, n+1):
        tot += min(mid // i, n)
    if tot < k:
        start = mid +1
    else:
        result = mid
        end = mid -1

print(result)