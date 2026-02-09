import sys
input = sys.stdin.readline

M = int(input().strip())

if M <= 2:
    print("NO")
    sys.exit()

ans = []

def add_block3(a):
    ans.append((1, a))
    ans.append((2, a + 1))
    ans.append((1, a + 2))
    ans.append((2, a))
    ans.append((1, a + 1))
    ans.append((2, a + 2))

def add_last4(a):
    ans.append((1, a))
    ans.append((2, a + 1))
    ans.append((1, a + 3))
    ans.append((2, a + 2))
    ans.append((1, a + 1))
    ans.append((2, a))
    ans.append((1, a + 2))
    ans.append((2, a + 3))

def add_last5(a):
    ans.append((1, a))
    ans.append((2, a + 1))
    ans.append((1, a + 3))
    ans.append((2, a + 4))
    ans.append((1, a + 2))
    ans.append((2, a))
    ans.append((1, a + 1))
    ans.append((2, a + 2))
    ans.append((1, a + 4))
    ans.append((2, a + 3))

r = M % 3

if r == 0:
    for a in range(1, M + 1, 3):
        add_block3(a)
elif r == 1:
    for a in range(1, M - 3, 3):
        add_block3(a)
    add_last4(M - 3)
else:
    for a in range(1, M - 4, 3):
        add_block3(a)
    add_last5(M - 4)

print("YES")
out = sys.stdout.write
for x, y in ans:
    out(f"{x} {y}\n")
