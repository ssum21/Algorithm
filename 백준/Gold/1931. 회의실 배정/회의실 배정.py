import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = []

for i in range(N):
    j, k = map(int, input().split())
    arr.append((j,k))

arr.sort(key=lambda x : (x[1], x[0]))

min_val=-1
tot=0
for start, end in arr:
    if(min_val<=start):
        min_val=end
        tot+=1

print(tot)