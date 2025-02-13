import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

min_lst = max(lst)
max_lst = sum(lst)
result = max_lst

while min_lst <= max_lst:
    avg_lst = (max_lst + min_lst) // 2
    sum = 0
    tot = 1

    for i in lst:
        if(sum + i > avg_lst):
            tot += 1
            sum = i
        else :
            sum += i
    
    if(tot > M): # 용량을 줄여야 하는 상태
        min_lst = avg_lst + 1
    else:
        result = avg_lst
        max_lst = avg_lst - 1
        
    
print(result)