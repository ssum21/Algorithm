import sys
input = sys.stdin.readline

#문제는 음수사이클이 존재하냐? 고 묻는 전형적인 벨만포드 문제
INF = sys.maxsize
tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split()) # 지점의 수, 도로의 개수, 웜홀의 개수
    graph = [[] for _ in range(n+1)]
    value = False
    for _ in range(m):
        s, e, t = map(int, input().split()) # s,e는 연결된 지점번호 t는 가중치
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, input().split()) # s,e는 연결된 지점번호 t는 감소가중치
        graph[s].append((e, -t))
    
    dist = [INF for _ in range(n+1)]
    dist[0] = 0
    for i in range(1, n+1):
        graph[0].append((i, 0))

    for i in range(1, n+1):
        for current_node in range(0, n+1):
            if dist[current_node] == INF:
                continue
            for next_node, weight in graph[current_node]:
                if dist[current_node] + weight < dist[next_node]:
                    dist[next_node] = dist[current_node] + weight
    for current_node in range(0, n+1):
        if dist[current_node] == INF:
            continue
        for next_node, weight in graph[current_node]:
            if dist[current_node] + weight < dist[next_node]:
                value = True
                break
        if value:
            break

    if value:
        print('YES')
    else:
        print('NO')

