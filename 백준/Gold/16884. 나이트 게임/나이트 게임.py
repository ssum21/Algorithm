import sys

T = int(input())

result = []
for _ in range(T):
    N = int(input())
    
    if N % 2 == 1:
        result.append("koosaga")
    else:
        result.append("cubelover")

print("\n".join(result))