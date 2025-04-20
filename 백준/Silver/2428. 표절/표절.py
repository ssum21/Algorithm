import sys
input=sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))
arr.sort()
l=0
ans=0
for r in range(N):
    while l<r and 10*arr[l]<9*arr[r]:
        l+=1
    ans+=r-l
print(ans)
