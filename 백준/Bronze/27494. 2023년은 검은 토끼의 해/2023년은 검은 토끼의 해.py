import sys
input = sys.stdin.readline

n = int(input())
target = '2023'
count = 0

for i in range(2023, n + 1):
    s = str(i)
    idx = 0
    for c in s:
        if c == target[idx]:
            idx += 1
            if idx == 4:
                count += 1
                break

print(count)
