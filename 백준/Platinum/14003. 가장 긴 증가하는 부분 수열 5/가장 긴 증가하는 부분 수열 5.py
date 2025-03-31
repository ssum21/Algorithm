import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

stack = []
stack_idx = []

dp_table = [1 for i in range(n+1)]
prev = [-1 for i in range(n+1)]

for i in range(n):
    if not stack or stack[-1]<lst[i]:
        stack.append(lst[i])
        if stack_idx:
            prev[i] = stack_idx[-1]
        stack_idx.append(i)
    else:
        k = bisect_left(stack, lst[i])
        stack[k] = lst[i]
        if k > 0:
            prev[i] = stack_idx[k-1]
        stack_idx[k] = i

k = len(stack)
idx = stack_idx[-1]
result = []
while idx!=-1:
    result.append(lst[idx])
    idx = prev[idx]

result.reverse()

print(k)
print(*result)