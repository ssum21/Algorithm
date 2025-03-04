import sys
import itertools
import math

# 입력 받기
N = int(sys.stdin.readline().strip())
problem = list(map(int, sys.stdin.readline().split()))

if problem[0] == 1:
    K = problem[1]
    nums = list(range(1, N + 1))
    result = []

    K -= 1  # 1-based index -> 0-based index

    for i in range(N, 0, -1):
        fact = math.factorial(i - 1)
        index = K // fact
        result.append(nums.pop(index))
        K %= fact
    
    print(*result)

elif problem[0] == 2:
    given_permutation = problem[1:]
    nums = list(range(1, N + 1))
    
    rank = 1  # 순서는 1부터 시작
    for i in range(N):
        index = nums.index(given_permutation[i])
        rank += index * math.factorial(N - i - 1)
        nums.pop(index)  # 사용된 숫자는 제거
    
    print(rank)
