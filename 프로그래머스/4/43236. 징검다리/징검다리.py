def solution(distance, rocks, n):
    rocks.sort()
    rocks = [0] + rocks + [distance]
    left, right = 1, distance # 가능한 간격
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        removed = 0 # 제거된 돌의 수
        prev = 0
        for i in range(1, len(rocks)):
            if(rocks[i] - rocks[prev] < mid):
                removed +=1
            else:
                prev = i
        if removed <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return answer