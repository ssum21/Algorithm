import sys
input = sys.stdin.readline

word = list(input().strip())
word2 = []

n = int(input().strip())

for _ in range(n):
    m = input().strip()
    if "L" in m:
        if word:
             word2.append(word.pop())
    elif "D" in m:
        if word2:
            word.append(word2.pop())                        
    elif "B" in m:
        if word:
            word.pop()
    else:
        word.append(m[2])

word2 = reversed(word2)
print(*word, *word2, sep="")