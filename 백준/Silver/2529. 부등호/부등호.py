import sys

input = sys.stdin.readline

N = int(input())
equal = list(map(str, input().split()))

def check(i, j, op):
    if op == '<':
        return i < j
    else:
        return i > j
    
def backtrack(idx, used, num):
    if idx == N + 1:
        return num, num
    max_num = ''
    min_num = '9' * (N + 1)
    for i in range(10):
        if not used[i]:
            if idx == 0 or check(num[-1], str(i), equal[idx - 1]):
                used[i] = True
                new_max, new_min = backtrack(idx + 1, used, num + str(i))
                if new_max > max_num:
                    max_num = new_max
                if new_min < min_num:
                    min_num = new_min
                used[i] = False
    return max_num, min_num

used = [False] * 10
max_num, min_num = backtrack(0, used, '')
print(max_num)
print(min_num)
