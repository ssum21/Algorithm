import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N - 1
min_abs = sys.maxsize
result = [arr[0], arr[-1]]

while left < right:
    current_sum = arr[left] + arr[right]
    
    if abs(current_sum) <= min_abs:
        min_abs = abs(current_sum)
        result = [arr[left], arr[right]]
    
    if current_sum == 0:
        break
    elif current_sum < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])
