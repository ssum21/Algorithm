import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())

isNumber = 0

trueman = list(map(int, input().split()))

human = [0] * (51)

def find(a):
    if (a==human[a]):
        return a
    else:
        human[a]=find(human[a])
        return human[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a != b:
        human[a] = b

for i in range(51):
    human[i] = i

trueman_set = []

if trueman[0]: # trueman 숫자 정상이라면,
    trueman_set = trueman[1:]


find_trueman_set=[]

for i in trueman_set:
    find_trueman_set.append(find(i))

#각 한 줄에 대해서 루트를 설정해주면 된다! 유니온을 통해서

lst = []
for i in range(M):
    temp = list(map(int, input().split()))
    lst.append(temp)
    if (temp[0]>1):
        for i in range(2, temp[0]+1):
            union(temp[1], temp[i])

find_trueman_set = {find(x) for x in trueman_set}

# 각 파티에서 대표 노드가 진실을 아는 그룹과 연결되지 않았는지 확인
for party in lst:
    if find(party[1]) not in find_trueman_set:
        isNumber += 1

print(isNumber)

