import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

nextA = [[-1] * 101 for _ in range(n+1)]
nextB = [[-1] * 101 for _ in range(m+1)]

for i in range(n-1, -1 ,-1):
    for num in range(1, 101):
        nextA[i][num] = nextA[i+1][num]
    nextA[i][A[i]] = i

for i in range(m-1, -1 ,-1):
    for num in range(1, 101):
        nextB[i][num] = nextB[i+1][num]
    nextB[i][B[i]] = i

result = []
i = j = 0
while i<n and j<m:
    found = False
    for num in range(100, 0, -1):
        posA = nextA[i][num]
        posB = nextB[j][num]
        if posA != -1 and posB != -1:
            result.append(num)
            i = posA+1
            j = posB+1
            found = True
            break
    if not found:
        break

print(len(result))
if result:
    print(" ".join(map(str, result)))