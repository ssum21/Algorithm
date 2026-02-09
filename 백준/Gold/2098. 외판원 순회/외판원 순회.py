import sys
sys.setrecursionlimit(10 ** 7)

def tsp(current, visited):
    global N, W, dp

    # ① 이미 계산한 상태면 바로 반환 (메모이제이션)
    if dp[current][visited] != -1:
        return dp[current][visited]

    # ② Base Case: 모든 도시를 방문한 경우
    if visited == (1 << N) - 1:
        if W[current][0] != 0:       # 시작점으로 돌아갈 수 있으면
            return W[current][0]
        else:                         # 돌아갈 수 없으면
            return sys.maxsize

    # ③ 방문하지 않은 도시들을 하나씩 시도
    min_cost = sys.maxsize
    for i in range(N):
        # 이미 방문한 도시이거나, 길이 없으면 스킵
        if visited & (1 << i) or W[current][i] == 0:
            continue

        # i번 도시로 이동 → 재귀적으로 나머지 탐색
        cost = tsp(i, visited | (1 << i)) + W[current][i]
        min_cost = min(min_cost, cost)

    # ④ 결과를 DP 테이블에 저장
    dp[current][visited] = min_cost
    return min_cost


def main():
    global N, W, dp

    input = sys.stdin.readline
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]

    # dp 테이블: N개 도시 × 2^N개 방문 상태, -1로 초기화
    dp = [[-1] * (1 << N) for _ in range(N)]

    # 0번 도시에서 출발, 0번 도시를 방문한 상태(= 1)로 시작
    print(tsp(0, 1))

if __name__ == "__main__":
    main()