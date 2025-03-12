case_num = 1

while True:
    L, P, V = map(int, input().split())
    if (L==0 and P==0 and V==0):
        break
    tot = 0
    week = V//P
    remainder = V % P
    result = week * L + min(remainder, L)
    print(f"Case {case_num}: {result}")
    case_num += 1

