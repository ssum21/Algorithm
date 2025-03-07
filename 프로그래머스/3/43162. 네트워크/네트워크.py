from collections import deque
from collections import defaultdict

def solution(n, computers):
    network = defaultdict(list)
    network_count = 0
    sum_visited = set()
    def make_graph(lst):
        len_lst = len(lst)
        for i in range(len_lst):
            for j in range(len_lst):
                if (i!=j and computers[i][j]):
                    network[i].append(j)
                    
    def BFS(start, graph):
        visited = set([start])
        queue = deque([start])
        while queue:
            now_value = queue.popleft()
            for neighbor in graph[now_value]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited
    make_graph(computers)
    for i in range(n):
        if i not in sum_visited:
            temp = BFS(i, network)
            for i in temp:
                sum_visited.add(i)
            network_count += 1
    
    return network_count