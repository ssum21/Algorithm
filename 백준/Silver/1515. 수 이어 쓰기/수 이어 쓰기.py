s = input()
n = 1
i = 0
while i < len(s):
    for c in str(n):
        if i < len(s) and s[i] == c:
            i += 1
    n += 1
print(n - 1)