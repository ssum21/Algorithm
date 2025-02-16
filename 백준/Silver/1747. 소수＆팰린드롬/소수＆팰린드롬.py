import sys
import math

input = sys.stdin.readline

def pellindrom(num):
    num = str(num)
    num_len = len(num) // 2
    for i in range(num_len):
        if(num[i]!=num[-(i+1)]):
            return False
    return True

def isPrime(num):
    if (num==1):
        return False
    for i in range(2, (int(math.sqrt(num))+1)):
        if num%i == 0:
            return False
    return True

N = int(input())

while True:
    if (isPrime(N) and pellindrom(N)):
        print(N)
        break
    else:
        N+=1
