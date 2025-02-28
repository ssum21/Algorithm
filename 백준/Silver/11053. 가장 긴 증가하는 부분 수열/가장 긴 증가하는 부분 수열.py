import sys
import math

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

def lis_length_dp(nums):
    dp = [1]*n  # dp[i] = nums[i]가 마지막 원소일 때 LIS 길이
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(lis_length_dp(a))