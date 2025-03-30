import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

def lis_length_dp(nums):
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp

def reverse_lis_length_dp(nums):
    dp = [1] * n

    for i in range(n-1,-1 , -1):
        for j in range(n-1, i-1, -1):
            if nums[i] > nums[j] :
                dp[i] = max(dp[i], dp[j]+1)
    return dp

left_arr = lis_length_dp(arr)
right_arr = reverse_lis_length_dp(arr)
sum_dp = [0 for _ in range(n)]

for i in range(n):
    sum_dp[i] = left_arr[i] + right_arr[i] - 1

print(max(sum_dp))