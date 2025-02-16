from collections import defaultdict

def solution(users, emoticons):
    answer = []
    poss_ratio = [40, 30, 20, 10]
    emoticons.sort()
    sum_emoticons = sum(emoticons)
    emoti_ratio = dict()
    index=0
    for each in emoticons:
        emoti_ratio[index]=[]
        emoti_ratio[index].append(each)
        for i in range(1, 5):
            emoti_ratio[index].append(each-(each*i//10))
        index+=1
        
    
    for ratio, price in users:
        if(sum_emoticons*6//10 < price)
        now_ratio = 40
        while now_ratio>=ratio
    
    print(emoti_ratio)
    
    return answer