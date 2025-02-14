def solution(prices):
    answer = [0] * len(prices)
    result = []
    stack =[]

    for i in range(len(prices)):
        # 가격이 떨어지는 경우 스택을 활용하여 유지 시간을 계산
        while stack and stack[-1][0] > prices[i]:
            price, index = stack.pop()
            answer[index] = i - index  # 유지된 시간 계산
        
        stack.append((prices[i], i))  # 현재 가격과 인덱스를 스택에 추가

    while stack:
        price, index = stack.pop()
        answer[index] = len(prices) - 1 - index

                
        
    return answer
