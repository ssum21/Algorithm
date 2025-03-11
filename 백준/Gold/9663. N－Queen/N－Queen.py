import sys

input = sys.stdin.readline

n = int(input().strip())

colUsed = [False] * (n)
diagUsed = [False] * ((2*n)-1)
AntidiagUsed = [False] * ((2*n)-1)

tot = 0

def placeQueens(row):
    global tot

    if (row == n):
        tot+=1
        return
    
    for col in range(n):
        diagIndex = row - col + n - 1 
        AntiDiagIndex = row + col

        if not colUsed[col] and not diagUsed[diagIndex] and not AntidiagUsed[AntiDiagIndex]:
            colUsed[col] = True
            diagUsed[diagIndex] = True
            AntidiagUsed[AntiDiagIndex] = True

            placeQueens(row + 1)

            colUsed[col] = False
            diagUsed[diagIndex] = False
            AntidiagUsed[AntiDiagIndex] = False


placeQueens(0)
print(tot)
