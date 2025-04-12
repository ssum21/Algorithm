N = int(input())
A = sorted(list(map(int, input().split())))

division_point = len(A) // 2

s = sum(A[:division_point])
p = sum(A[division_point:])

print(s, p)
