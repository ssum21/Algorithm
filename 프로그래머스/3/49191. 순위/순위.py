def solution(n, results):
    # wins[i][j]는 i번 선수가 j번 선수를 이겼음을 의미
    wins = [[False] * (n + 1) for _ in range(n + 1)]
    
    # 주어진 경기 결과로 직접 승리한 관계 초기화
    for winner, loser in results:
        wins[winner][loser] = True
    
    # Floyd–Warshall 알고리즘으로 전이적 승리 관계 계산
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if wins[i][k] and wins[k][j]:
                    wins[i][j] = True
    
    answer = 0
    # 각 선수에 대해 다른 모든 선수와의 승패 관계 확인
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            # i가 j를 이기거나, j가 i를 이겼다면 관계가 결정됨
            if wins[i][j] or wins[j][i]:
                count += 1
        # 모든 다른 선수와의 관계가 결정되면 순위 확정 가능
        if count == n - 1:
            answer += 1
    
    return answer
