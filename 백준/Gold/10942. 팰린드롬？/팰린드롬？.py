import sys

ssr = sys.stdin.readline

N = int(ssr())
nums = list(map(int, ssr().split()))
M = int(ssr())

answer = [[0] * N for _ in range(N)]

for i in range(N):
    for head in range(N):
        tail = head + i
        
        #존재하지 않는 문자열
        if tail >= N:
            break
		
        #문자열의 길이가 1인 경우
        if i == 0:
            answer[head][tail] = 1
            continue

		#문자열의 길이가 2인 경우
        if i == 1:
            if nums[head] == nums[tail]:
                answer[head][tail] = 1
                continue
                
		#문자열의 길이가 2보다 긴 경우
        if nums[head] == nums[tail] and answer[head + 1][tail - 1]:
            answer[head][tail] = 1


for i in range(M):
    S, E = map(int, ssr().split())
    print(answer[S-1][E-1])