import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
orig = list(map(int, input().split()))

for start in orig:
    arr = deque(orig)
    answer = deque()

    arr.remove(start)
    cur = start
    answer.append(cur)

    while arr:
        # 1) /3 우선
        if cur % 3 == 0:
            div_value = cur // 3
            if div_value in arr:
                arr.remove(div_value)
                cur = div_value
                answer.append(cur)
                continue

        # 2) *2
        mul_value = cur * 2
        if mul_value in arr:
            arr.remove(mul_value)
            cur = mul_value
            answer.append(cur)
            continue

        # 다음 값이 없으면 이 start는 실패
        break

    if len(answer) == N:
        print(' '.join(map(str, answer)))
        break
