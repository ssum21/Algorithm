import sys
from collections import defaultdict
import math
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
case = 0

def BFS(start, end):
    queue = deque([(start, 1)])
    visited = set([start])
    while queue:
        k, chance = queue.popleft()
        if k == end:
            return chance
        temp1 = int(str(k) + '1')  # 1을 추가한 값
        temp2 = k * 2  # 2를 곱한 값

        # 두 가지 연산을 수행하고 큐에 추가 (범위 초과 방지)
        if temp1 <= end and temp1 not in visited:
            visited.add(temp1)
            queue.append((temp1, chance + 1))
        
        if temp2 <= end and temp2 not in visited:
            visited.add(temp2)
            queue.append((temp2, chance + 1))

    return -1  # 만들 수 없는 경우

print(BFS(a,b))