import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    a = input().strip()
    b = input().strip()

    result = 0

    for i in range(len(a)):
        if a[i]!=b[i]:
            result += 1

    print('Hamming distance is ' + str(result) + '.')