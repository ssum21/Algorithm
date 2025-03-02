import sys

input = sys.stdin.readline

n = int(input())
total = 0 
result = 0
visited = [[False]*n for i in range(n)]
arr = []
for i in range(n):
    arr.append(list(input().rstrip()))

edge_list = []

for i in range(n):
    for j in range(n):
        k = arr[i][j]
        if 'a' <= k <= 'z':
            arr[i][j] = ord(k) - ord('a') + 1
        elif 'A' <= k <= 'Z':
            arr[i][j] = ord(k) - ord('A') + 27
        elif k=='0':
            arr[i][j] = int(k)
        edge_list.append((arr[i][j], i, j))
        result += arr[i][j]
        

we_arr = [i for i in range(n+1)]
        
def find(a):
    if(we_arr[a]==a):
        return a
    else:
        we_arr[a] = find(we_arr[a])
        return we_arr[a]
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        we_arr[b] = a
    elif a>b:
        we_arr[a] = b

edge_list.sort(key=lambda x:x[0])
temp = 0

for weight, y, x in edge_list:
    if not visited[x][y] and arr[y][x] != 0:
        if find(y) != find(x):
            temp += 1
            visited[x][y] = True
            union(x, y)
            total += weight
            

if temp == n-1:
    print(result - total)
else:
    print(-1)

           