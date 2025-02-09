def solution(clothes):
    arr=[]
    temp=2
    answer = 1
    clothes.sort(key = lambda x:(x[1], x[0]))
    maxvalue = len(clothes)
    for i in range(0, maxvalue-1):
        if (clothes[i][1] != clothes[i+1][1]):
            arr.append(temp)
            temp=2
        else:
            temp+=1
    arr.append(temp)
    for j in arr:
        answer *= j
    answer -= 1
    return answer


