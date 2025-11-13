import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
stack = []
ans = [0] * n

for i in range(n):
    while stack and li[stack[-1]] < li[i]:
        ans[stack.pop()] = li[i]
    stack.append(i)

while stack:
    ans[stack.pop()] = -1

print(" ".join(map(str, ans)))
