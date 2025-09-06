import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

left_index = 0
right_index = n-1
total = 0

while left_index < right_index:
    sum_tmp = arr[left_index] + arr[right_index]
    if sum_tmp == x:
        total += 1
        left_index += 1
        right_index -= 1
    elif sum_tmp > x:
        right_index -= 1
    else:
        left_index += 1

print(total)
