import math
from itertools import permutations

prime_check = [False] * 10000000

def isPrime(number):
    print(number)
    if(prime_check[number]==True):
        return False
    if(number == 0 or number == 1):
        return False
    for temp in range(2, int(math.sqrt(number))+1):
        if(number%temp==0):
            return False # 소수 아님
    prime_check[number]=True
    return True # 소수
    

def solution(numbers):
    answer = 0
    name = str()
    number_paper = []
    for i in numbers:
        number_paper.append(i)
    for j in range(1, len(number_paper)+1):
        nPr = permutations(number_paper, j)
        for k in nPr:
            name = str()
            for m in k:
                name += m
            if isPrime(int(name)):
                answer+=1
    return answer