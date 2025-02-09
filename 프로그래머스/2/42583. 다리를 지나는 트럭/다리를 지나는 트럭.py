from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque()
    index = 0
    seconds = 0
    maxvalue=len(truck_weights)-1
    now_weight=0
    for _ in range(bridge_length):
        queue.append(0)
    while True:
        seconds+=1
        now_weight-=queue.popleft()
        if(now_weight+truck_weights[index] <= weight):
            queue.append(truck_weights[index])
            now_weight+=truck_weights[index]
            if(index==maxvalue):
                seconds+=bridge_length
                break
            else:
                index+=1
        else:
            queue.append(0)
        if(now_weight == 0):
            break
    return seconds