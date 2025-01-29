import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())
A = list([] for i in range(N+1))
tot=0

visited = [0] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)


def DFS(v):
    visited[v] = True
    for i in A[v]:
        if(visited[i]==False):
            DFS(i)


for i in range(1,N+1):
    if(visited[i]==False):
        tot+=1
        DFS(i)

print(tot)