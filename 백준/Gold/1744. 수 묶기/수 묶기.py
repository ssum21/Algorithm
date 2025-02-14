import heapq
import sys
from collections import deque

input = sys.stdin.readline

maxheap=[]
minheap=[]
result = 0
count_0 = 0
count_1 = 0
N = int(input().rstrip())

def plusnum(num):
    maxheap.append(num)

def minusnum(num):
    minheap.append(num)

for i in range(N):
    num = int(input().rstrip())
    if(num==0):
        count_0 += 1
    elif(num==1):
        count_1 += 1
    elif(num>0):
        plusnum(num)
    else:
        minusnum(num)

maxheap.sort()
minheap.sort()

while maxheap:
    first_value = maxheap.pop()
    if maxheap:
        second_value = maxheap.pop()
        result += (first_value * second_value)
    else:
        result += first_value

if (len(minheap)%2==1):
    if count_0 and minheap:
        minheap.pop()
    else:
        result+=minheap.pop()

while minheap:
    first_value = minheap.pop()
    second_value = minheap.pop()
    result += (first_value * second_value)

result+=count_1

print(result)


