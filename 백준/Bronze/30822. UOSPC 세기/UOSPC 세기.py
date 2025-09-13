import sys
from collections import Counter

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

char_counts = Counter(s)

count_u = char_counts['u']
count_o = char_counts['o']
count_s = char_counts['s']
count_p = char_counts['p']
count_c = char_counts['c']

result = min(count_u, count_o, count_s, count_p, count_c)

print(result)
