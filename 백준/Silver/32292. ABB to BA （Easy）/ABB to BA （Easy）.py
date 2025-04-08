t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    i = 0
    while i <= len(s) - 3:
        if s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'B':
            s[i], s[i + 1] = 'B', 'A'
            s.pop(i + 2)
            i = max(i - 2, 0)
        else:
            i += 1
    print(''.join(s))
