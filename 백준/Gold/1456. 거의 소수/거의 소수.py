import sys
import math

input = sys.stdin.readline

Min, Max = map(int, input().split())
A = [0]*10000001

for i in range(len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)))+1):
    if A[i]==0:
        continue
    for j in range(i+i, len(A), i):
        A[j] = 0

count = 0

for i in range(2, 10000001):
    if A[i]!= 0:
        temp = A[i]
        while A[i] <= Max / temp:
            if A[i] >= Min / temp:
                count +=1
            temp = temp * A[i]

print(count)