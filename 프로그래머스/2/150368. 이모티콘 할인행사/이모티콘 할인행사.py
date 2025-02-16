from collections import defaultdict

def DFS(idx, config, emoji_count, poss_ratio):
    # 기저 조건: 모든 이모티콘에 대해 할인율을 정했다면
    if idx == emoji_count:
        evaluate_config(config)  # 이 할인율 조합에 대해 사용자 시뮬레이션
        return

    # 백트래킹: 각 이모티콘에 대해 가능한 모든 할인율 시도
    for discount in poss_ratio:
        config.append(discount)           # 현재 이모티콘에 discount 할당
        DFS(idx + 1, config, emoji_count, poss_ratio)  # 다음 이모티콘으로 진행
        config.pop()                      # 할당 취소(백트래킹)


# 전역 변수 (최종 결과)
max_plus = 0
max_sales = 0

def evaluate_config(config):
    global max_plus, max_sales
    plus_count = 0
    sales = 0
    # 각 사용자를 순회
    for min_discount, price_threshold in users:  # users는 전역 또는 매개변수로 전달
        total_cost = 0
        # 모든 이모티콘에 대해 할인율과 할인 가격 계산
        for i in range(len(emoticons)):
            discount = config[i]
            # 사용자가 관심 있는 할인율만 구매 (예: discount >= min_discount)
            if discount >= min_discount:
                discounted_price = emoticons[i] * (100 - discount) // 100
                total_cost += discounted_price
        # 기준 가격에 따른 플러스 가입 여부 결정
        if total_cost >= price_threshold:
            plus_count += 1
        else:
            sales += total_cost
    
    # 전역 결과 갱신 (가입자 우선, 매출액 두번째)
    if plus_count > max_plus or (plus_count == max_plus and sales > max_sales):
        max_plus = plus_count
        max_sales = sales

    

def solution(users_input, emoticons_input):
    global users, emoticons, max_plus, max_sales
    users = users_input
    emoticons = emoticons_input
    max_plus = 0
    max_sales = 0

    poss_ratio = [40, 30, 20, 10]
    emoji_count = len(emoticons)

    DFS(0, [], emoji_count, poss_ratio)

    return [max_plus, max_sales]
