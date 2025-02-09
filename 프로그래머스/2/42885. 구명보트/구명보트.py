def solution(people, limit):
    people.sort()  # 오름차순 정렬 (가벼운 사람부터)
    left, right = 0, len(people) - 1  # 투 포인터 설정
    boats = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:  # 가장 가벼운 사람과 가장 무거운 사람이 같이 탈 수 있는 경우
            left += 1  # 가벼운 사람도 태움
        right -= 1  # 무거운 사람 태움
        boats += 1  # 보트 사용 카운트
        
    return boats
