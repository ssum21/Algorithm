import sys
input=sys.stdin.readline
n=int(input())
A=list(map(int,input().split()))
U,D=map(int,input().split())
count1=A.count(1)
count2=A.count(2)
if count1>U or count2>D:
    print("NO")
    sys.exit()
U-=count1
D-=count2
res=[]
for a in A:
    if a==1:
        res.append('U')
    elif a==2:
        res.append('D')
    else:
        if U>0:
            res.append('U')
            U-=1
        else:
            res.append('D')
            D-=1
print("YES")
print(''.join(res))
