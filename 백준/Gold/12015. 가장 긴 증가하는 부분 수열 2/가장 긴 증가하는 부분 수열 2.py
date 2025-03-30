from bisect import bisect_left
import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
stack = []

for i in lst:
    if not stack or stack[-1] < i:
        stack.append(i)
    else:
        a = bisect_left(stack, i)
        stack[a] = i

print(len(stack))