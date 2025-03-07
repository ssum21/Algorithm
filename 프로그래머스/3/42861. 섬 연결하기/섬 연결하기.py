def solution(n, costs):
    # Union-Find 초기화: 각 섬은 자기 자신을 부모로 갖는다.
    parent = list(range(n))
    
    # find 함수: 경로 압축을 적용하여 부모를 찾는다.
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    # union 함수: 두 노드가 다른 집합에 속하면 합치고 True 반환
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False
    
    # 비용 오름차순으로 정렬
    costs.sort(key=lambda x: x[2])
    
    total_cost = 0
    edges_used = 0
    for start, end, cost in costs:
        if union(start, end):
            total_cost += cost
            edges_used += 1
            if edges_used == n - 1:
                break
    return total_cost
