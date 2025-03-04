import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# dp_no[i] : i번째 원소까지 고려할 때, 한 개도 삭제하지 않고 선택한 연속 부분합의 최댓값
# dp_del[i] : i번째 원소까지 고려할 때, 한 개의 원소를 삭제한 상태에서의 연속 부분합의 최댓값
dp_no = [0] * n
dp_del = [0] * n

dp_no[0] = a[0]
dp_del[0] = -10**9  # 매우 작은 값으로 초기화 (첫 원소를 제거하면 빈 구간이 되어버리므로)

result = a[0]
for i in range(1, n):
    dp_no[i] = max(a[i], dp_no[i-1] + a[i])
    dp_del[i] = max(dp_del[i-1] + a[i], dp_no[i-1])
    result = max(result, dp_no[i], dp_del[i])

print(result)
