import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

# 1. 그래프 입력
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

# 2. kmax 계산 (2^k >= N 만족하는 k)
kmax = 0
temp = 1
while temp <= N:
    temp <<= 1
    kmax += 1

depth = [0] * (N+1)
visited = [False] * (N+1)
parent = [[0] * (N+1) for _ in range(kmax+1)]

# 3. BFS로 depth, parent[0] 채우기
def BFS(start):
    queue = deque([start])
    visited[start] = True
    level = 1
    count = 0
    now_size = 1
    
    while queue:
        node = queue.popleft()
        for nxt in tree[node]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
                parent[0][nxt] = node  # 바로 윗 조상 기록
                depth[nxt] = level
        count += 1
        if count == now_size:
            count = 0
            now_size = len(queue)
            level += 1

BFS(1)  # 루트(1번 노드)부터 BFS

# 4. parent[k][v]: v에서 2^k 위에 있는 조상 전처리
for k in range(1, kmax+1):
    for v in range(1, N+1):
        parent[k][v] = parent[k-1][ parent[k-1][v] ]

# 5. LCA(최소공통조상) 함수
def LCA(a, b):
    # depth[a] <= depth[b]가 되도록 조정
    if depth[a] > depth[b]:
        a, b = b, a
    
    # b를 a와 depth가 같아질 때까지 끌어올리기
    diff = depth[b] - depth[a]
    for k in range(kmax+1):
        if diff & (1 << k):
            b = parent[k][b]
    
    # 만약 a와 b가 같다면 그게 LCA
    if a == b:
        return a
    
    # 가장 높은 레벨부터, 부모가 서로 다를 때만 끌어올리기
    for k in range(kmax, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    
    # 마지막에 한 칸(직계 부모) 올리면 LCA
    return parent[0][a]

# 6. 쿼리 처리
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(str(LCA(a, b)) + '\n')
