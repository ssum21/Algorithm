import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, r, c = map(int, input().split())

def squared(n, r, c, tot):
    next_right, next_height = 2** n, 2** n
    if(n==1 and r==0 and c==0):
        return tot
    elif(n==1 and r==0 and c==1):
        return tot+1
    elif(n==1 and r==1 and c==0):
        return tot+2
    elif(n==1 and r==1 and c==1):
        return tot+3
    if (r<next_right//2 and c <next_height//2):
        return squared(n-1, r, c, tot)
    elif (r<next_right//2):
        return squared(n-1, r, c-(2**(n-1)), tot+2 ** (2*n-2))
    elif (c<next_height//2):
        return squared(n-1, r-(2**(n-1)), c, tot + 2 ** (2*n-1))
    else:
        return squared(n-1, r-(2**(n-1)), c-(2**(n-1)), tot + (2 ** (2*n-2) + 2 ** (2*n-1)))

print(squared(N, r, c, 0))
