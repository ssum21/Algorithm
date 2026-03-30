import sys
from collections import defaultdict, deque
from heapq import heapify, heappush, heappop

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
tot = 0

cols = [False] * N
diag1 = [False] * (2*N-1)
diag2 = [False] * (2*N-1)

def Backtrack(Length):
    global tot
    if (Length == N):
        tot += 1
        return
    
    for i in range(N):
        if not cols[i] and not diag1[i+Length] and not diag2[i-Length+N-1]:
            cols[i] = diag1[i+Length] = diag2[i-Length+N-1] = True
            Backtrack(Length+1)
            cols[i] = diag1[i+Length] = diag2[i-Length+N-1] = False

Backtrack(0)
print(tot)