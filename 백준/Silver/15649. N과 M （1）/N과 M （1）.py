import sys
from collections import defaultdict, deque
from heapq import heapify, heappush, heappop

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * N
S = [0] * M

def backtrack(length):
    if length == M:
        a = " ".join(str(x+1) for x in S)
        print(a)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            S[length] = i
            backtrack(length+1)
            visited[i] = False

backtrack(0)
