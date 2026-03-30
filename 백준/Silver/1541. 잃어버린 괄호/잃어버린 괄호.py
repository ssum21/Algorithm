import sys
from collections import defaultdict, deque
from heapq import heapify, heappush, heappop

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

A = list(map(str, input().split('-')))

def mysum(i):
    sum = 0
    temp = str(i).split('+')
    for i in temp:
        sum += int(i)
    return sum

answer = 0

for i in range(len(A)):
    temp = mysum(A[i])
    if i ==0:
        answer += temp
    else:
        answer -= temp

print(answer)