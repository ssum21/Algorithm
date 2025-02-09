def solution(citations):
    answer = 0
    for i in range(len(citations),-1,-1):
        temp = 0
        for j in citations:
            if(i<=j):
                temp +=1
        if (temp >= i):
            answer = i
            break
    return answer