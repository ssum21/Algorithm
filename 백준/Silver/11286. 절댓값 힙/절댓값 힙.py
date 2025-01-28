import sys
from queue import PriorityQueue

pq = PriorityQueue()
num = int(sys.stdin.readline().rstrip())

for i in range(num):
    temp = int(sys.stdin.readline().rstrip())
    if(temp==0 and pq.empty()):
        print('0')
    elif(temp==0):
        print(pq.get()[1])
    else:
        pq.put((abs(temp),temp))