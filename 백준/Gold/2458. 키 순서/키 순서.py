import sys

input = sys.stdin.readline

N, M = map(int,input().split()) # 학생들의 수 N, 두 학생의 키를 비교한 횟수 M

tall = [[False for i in range(N+1)] for j in range(N+1)]

for i in range(M):
    small, big = map(int, input().split())
    tall[small][big] = True

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if tall[i][k] and tall[k][j]:
                tall[i][j] = True

answer = 0

for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if i==j:
            continue
        if tall[i][j] or tall[j][i]:
            count += 1
    if count == N-1:
        answer += 1

print(answer)