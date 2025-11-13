a=int(input())
tot = 0
b=[]

for i in range(a):
    b = list(input().rstrip())
    tot=len(b)
    temp=0
    for j in range(tot):
        if(b[j]=='('):
            temp+=1
        else:
            temp-=1
        if(temp<0):
            break
    if(temp==0):
        print("YES")
    else:
        print("NO")
