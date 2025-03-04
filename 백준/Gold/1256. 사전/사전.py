import math
import sys
from itertools import permutations

input = sys.stdin.readline

N, M, K = map(int, input().split())

total = math.comb(N+M, N)

if K>total:
    print(-1)
else:
    result = []
    while N > 0 and M > 0:
        count = math.comb(N+M-1, N-1)
        if K<=count:
            result.append('a')
            N -= 1
        else:
            result.append('z')
            M -= 1
            K -= count
    
    result.extend(["a"] * N)
    result.extend(["z"] * M)

    print("".join(result))
    