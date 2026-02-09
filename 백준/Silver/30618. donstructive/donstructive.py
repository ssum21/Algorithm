import sys
input = sys.stdin.readline

n = int(input())
odds  = list(range(1, n + 1, 2))          # 1,3,5,...
evens = list(range(2, n + 1, 2))[::-1]     # ...,4,2  (내림차순)
ans = odds + evens
print(*ans)