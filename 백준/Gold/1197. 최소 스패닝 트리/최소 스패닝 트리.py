import sys
import math
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V, E = map(int, input().split())
a = []
uf_arr = [0]
distance = 0
for i in range(1, V+1):
    uf_arr.append(i)

def find(a):
    if(a==uf_arr[a]):
        return a
    else:
        uf_arr[a] = find(uf_arr[a])
        return uf_arr[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if(a!=b):
        uf_arr[b] = a

for i in range(E):
    s, e, w = map(int, input().split())
    a.append((w, s, e)) # 가중치, 시작점, 종료점

a.sort(key=lambda x : x[0])
edge_count = 0

for w, s, e in a:
    if(find(s) != find(e)):
        union(s, e)
        distance += w
        edge_count += 1
        if edge_count >= V-1:
            break

print(distance)