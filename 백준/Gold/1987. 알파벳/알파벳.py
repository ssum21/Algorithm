import sys

# 상하좌우 이동 좌표
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 입력 받기
r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(r)]

# 방문한 알파벳을 체크할 배열 (26개 알파벳)
visited_alpha = [False] * 26

# 최대 경로 길이를 저장할 변수
answer = 0

def dfs(x, y, count):
    global answer
    answer = max(answer, count)  # 현재까지의 경로 길이 중 최대값 갱신

    for i in range(4):  # 4방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            next_alpha = ord(graph[nx][ny]) - ord('A')
            if not visited_alpha[next_alpha]:  # 아직 방문하지 않은 알파벳이라면
                visited_alpha[next_alpha] = True
                dfs(nx, ny, count + 1)
                visited_alpha[next_alpha] = False  # 백트래킹 (되돌리기)

# 시작 위치의 알파벳 방문 체크
visited_alpha[ord(graph[0][0]) - ord('A')] = True

# DFS 시작
dfs(0, 0, 1)

# 정답 출력
print(answer)
