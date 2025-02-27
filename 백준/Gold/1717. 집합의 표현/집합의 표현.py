import sys

input = sys.stdin.readline

n,m = map(int, input().split())

def union(a, b):
    a = find(a)
    b = find(b)
    if a!=b:
        lst[b] = a

def find(a):
    if(a==lst[a]):
        return a
    else:
        lst[a] = find(lst[a])
        return lst[a]
    
def checkSame(a,b):
    a = find(a)
    b = find(b)
    if(a==b):
        return True
    return False

lst = []
for i in range(1000001):
    lst.append(i)

for _ in range(m):
    check, a, b = map(int, input().split())

    if check == 0:
        union(a,b)
    else:
        if checkSame(a,b):
            print("YES")
        else:
            print("NO")