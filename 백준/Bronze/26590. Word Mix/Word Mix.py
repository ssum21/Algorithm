import sys

word1, word2 = sys.stdin.readline().strip().split()

min_len = min(len(word1), len(word2))
result = []

for i in range(min_len):
    if i % 2 == 0:
        result.append(word1[i])
    else:
        result.append(word2[i])

print(''.join(result))
