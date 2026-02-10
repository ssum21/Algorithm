import sys

data = sys.stdin.buffer.read()
p = 0
L = len(data)

def readint():
    global p
    while p < L and data[p] <= 32:
        p += 1
    num = 0
    while p < L and data[p] > 32:
        num = num * 10 + (data[p] - 48)
        p += 1
    return num

N = readint()

a0 = readint()
a1 = readint()

NEG = -10**30

minA = a0
best1 = a1 - minA
minA = a1 if a1 < minA else minA

best2 = NEG
ans = NEG

for t in range(2, N):
    x = readint()

    if t >= 3:
        v = best2 + x
        if v > ans:
            ans = v

    v2 = best1 - x
    if v2 > best2:
        best2 = v2

    v1 = x - minA
    if v1 > best1:
        best1 = v1

    if x < minA:
        minA = x

sys.stdout.write(str(ans) + "\n")
