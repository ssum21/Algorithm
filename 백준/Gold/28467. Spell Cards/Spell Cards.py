import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# N=1인 경우는 합칠 필요가 없으므로 비용 0
if n <= 1:
    print(0)
else:
    total_mana = 0
    current_cards = list(arr) # 원본 리스트를 복사하여 사용

    # 카드가 하나 남을 때까지 반복
    while len(current_cards) > 1:
        min_sum = sys.maxsize
        merge_index = -1

        # 인접한 두 카드의 합 중 최소값 찾기
        for i in range(len(current_cards) - 1):
            current_sum = current_cards[i] + current_cards[i+1]
            if current_sum < min_sum:
                min_sum = current_sum
                merge_index = i # 합칠 왼쪽 카드 인덱스

        # 최소 합을 갖는 두 카드 합치기
        total_mana += min_sum # 합치는 비용 누적

        # 새로운 카드 생성 (두 카드 중 최대값)
        max_value = max(current_cards[merge_index], current_cards[merge_index+1])

        # 리스트 업데이트: 왼쪽 카드를 새로운 카드로 바꾸고 오른쪽 카드 삭제
        current_cards[merge_index] = max_value
        del current_cards[merge_index + 1]

    # 최종 누적된 마력 소모량 출력
    print(total_mana)