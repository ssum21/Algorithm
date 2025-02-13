import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 최소 용량은 모든 레슨 중 가장 긴 레슨의 길이여야 함
min_lst = max(lst)
# 최대 용량은 모든 레슨의 합
max_lst = sum(lst)
result = max_lst

while min_lst <= max_lst:
    # 후보 용량(mid)을 구함
    avg_lst = (min_lst + max_lst) // 2
    tot = 1  # 구간(블루레이)의 개수; 첫 번째 구간부터 시작
    temp = 0  # 현재 구간의 합

    # 각 레슨을 순회하며 현재 용량(avg_lst)으로 몇 개의 구간이 필요한지 계산
    for i in lst:
        if temp + i > avg_lst:
            tot += 1      # 현재 구간에 넣을 수 없으므로 새 구간 시작
            temp = i
        else:
            temp += i

    # M개보다 많은 구간이 필요하면 용량이 부족한 것이므로, 후보 용량을 늘린다.
    if tot > M:
        min_lst = avg_lst + 1
    else:
        # M개 이하이면 후보 용량을 줄여서 최소값을 찾는다.
        result = avg_lst
        max_lst = avg_lst - 1

print(result)