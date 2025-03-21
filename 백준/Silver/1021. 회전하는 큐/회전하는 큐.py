import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
answer_q = deque(map(int ,input().split()))
q = deque()

for i in range(1, n+1):
    q.append(i)

chance = 0

while answer_q:
    k = answer_q.popleft()
    if (k == q[0]):
        q.popleft()
    elif(q.index(k)<=len(q)//2):
        while(k!=q[0]):
            temp = q.popleft()
            q.append(temp)
            chance += 1
        q.popleft()
    else:
        while(k!=q[0]):
            temp = q.pop()
            q.appendleft(temp)
            chance += 1
        q.popleft()

print(chance)