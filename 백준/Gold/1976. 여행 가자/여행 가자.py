import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

is_poss = True

N = int(input())
M = int(input())

city = [0] * (201)

for i in range(201):
    city[i] = i

def find(a):
    if (a==city[a]):
        return a
    else:
        a = find(city[a])
        return a
    
def union(a,b):
    a = find(a)
    b = find(b)
    city[a] = b

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if(arr[i][j]==1):
            union(i+1, j+1)

visitTrip = list(map(int, input().split()))

num = visitTrip[0]

# 4) 첫 번째 도시의 루트를 기준으로 해서
root = find(visitTrip[0])

# 5) 나머지 도시가 전부 같은 루트인지 검사
possible = True
for i in range(1, M):
    if find(visitTrip[i]) != root:
        possible = False
        break

print("YES" if possible else "NO")