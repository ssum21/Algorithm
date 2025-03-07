def solution(money):
    n = len(money)
    if n == 1:
        return money[0]
    
    def rob_linear(arr):
        dp = [0] * len(arr)
        dp[0] = arr[0]
        if len(arr) >= 2:
            dp[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            dp[i] = max(dp[i-1], dp[i-2] + arr[i])
        return dp[-1]
    
    # 첫 번째 집 포함, 마지막 집 제외
    case1 = rob_linear(money[:-1])
    # 첫 번째 집 제외, 마지막 집 포함
    case2 = rob_linear(money[1:])
    
    return max(case1, case2)
