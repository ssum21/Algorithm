import sys
input = sys.stdin.readline

N = int(input())
M = [None]  # 1-indexed를 위해 더미 삽입
for i in range(N):
    r, c = map(int, input().split())
    M.append((r, c))

# D[s][e]: 행렬 s~e를 곱하는 최소 연산 횟수 (-1이면 아직 미계산)
D = [[-1] * (N + 1) for _ in range(N + 1)]

def solve(s, e):
    # 이미 계산했으면 바로 반환 (메모이제이션)
    if D[s][e] != -1:
        return D[s][e]

    # Base Case 1: 행렬 1개 → 곱셈 불필요
    if s == e:
        return 0

    # Base Case 2: 행렬 2개 → 바로 곱하기
    if s + 1 == e:
        D[s][e] = M[s][0] * M[s][1] * M[e][1]
        return D[s][e]

    # Recursive Case: 모든 분할 지점 k 시도
    result = sys.maxsize
    for k in range(s, e):
        cost = (
            solve(s, k)              # 왼쪽 구간 비용
            + solve(k + 1, e)        # 오른쪽 구간 비용
            + M[s][0] * M[k][1] * M[e][1]  # 두 결과를 합치는 비용
        )
        result = min(result, cost)

    D[s][e] = result
    return result

print(solve(1, N))