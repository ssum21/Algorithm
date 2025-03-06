def solution(N, number):
    # dp[i]는 N을 i번 사용해서 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        # N을 i번 이어 붙인 수 (예: N=5, i=3이면 555)
        dp[i].add(int(str(N) * i))
        
        # 가능한 경우의 수: j와 i-j로 나누어 연산
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
        
        # 목표 number가 현재 집합에 포함되어 있으면, i 반환
        if number in dp[i]:
            return i

    return -1
