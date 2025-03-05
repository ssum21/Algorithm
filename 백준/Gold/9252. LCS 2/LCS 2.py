import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

A = list(map(str, input().rstrip()))
B = list(map(str, input().rstrip()))

len_A = len(A)
len_B = len(B)

arr = [[0 for i in range(len_B+1)] for j in range(len_A+1)]

for i in range(1, len_A+1):
    for j in range(1, len_B+1):
        if(A[i-1] == B[j-1]):
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

print(arr[len_A][len_B])

result = []

def getText(r, c):
    if r==0 or c==0:
        return
    if A[r-1] == B[c-1]:
        result.append(A[r-1])
        getText(r-1, c-1)
    else:
        if arr[r-1][c] > arr[r][c-1]:
            getText(r-1,c)
        else:
            getText(r, c-1)

getText(len_A, len_B)
result_reverse = []

for i in range(len(result)):
    result_reverse.append(result.pop())

print(('').join(result_reverse))
