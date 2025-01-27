import sys

A, B, C, M = map(int, input().split(' '))

tired = 0
work = 0

def promising(i):
    if(tired+A>M):
        return False
    else:
        return True


for i in range(24):
    if(promising(i)):
        work += B
        tired += A
    else:
        tired-=C
        if(tired<0):
            tired=0

print(work)
