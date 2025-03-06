import sys

def solution(n, times):
    min_value, max_value = 0, max(times)*n
    answer = max_value

    while min_value<=max_value:
        mid = (max_value + min_value) // 2
        poss = 0
        for time in times:
            poss += mid // time
    
        if poss >= n:
            answer = mid
            max_value = mid - 1
            
        else:
            min_value = mid + 1
            
    return answer