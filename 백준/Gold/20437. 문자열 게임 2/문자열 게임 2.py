import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline
max_value = sys.maxsize

T = int(input())
window = deque()

for _ in range(T):
    W = input().rstrip()
    K = int(input())
    # 어떤 문자를 정확히 K를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
    
    dic = defaultdict(list)

    for i in range(len(W)):
        if W.count(W[i])>=K:
            dic[W[i]].append(i)
    
    if not dic:
        print(-1)
        continue
    else:
        small_length = max_value
        big_length = -1

        for key in dic:
            for i in range(len(dic[key]) - K + 1):
                length = dic[key][i + K - 1] - dic[key][i] + 1
                if length < small_length:
                    small_length = length
                if length > big_length:
                    big_length = length

        print(small_length, big_length)


