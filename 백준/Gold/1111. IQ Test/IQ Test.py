import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print('A')
elif n == 2:
    # n이 2일 때 두 수가 같으면 그 수, 다르면 A를 출력
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print('A')
elif arr[1] == arr[0]:
    flag = False
    for i in range(1, n):
        if arr[i] != arr[0]:
            flag = True
    if flag:
        print('B')
    else:
        print(arr[0])
elif n > 2 and arr[2] - arr[1] == arr[1] - arr[0]:
    d = arr[1] - arr[0]
    flag = False
    for i in range(1, n):
        if arr[i] - arr[i-1] != d:
            flag = True
    if flag:
        print('B')
    else:
        print(arr[n-1] + d)
elif n > 2 and arr[0] != 0 and arr[1] % arr[0] == 0 and arr[1] != 0 and arr[2] % arr[1] == 0 and arr[2] // arr[1] == arr[1] // arr[0]:
    # 등비수열 체크 (정확히 나누어 떨어지는지 확인)
    r = arr[1] // arr[0]
    flag = False
    for i in range(1, n):
        if arr[i-1] == 0 or arr[i] % arr[i-1] != 0 or arr[i] // arr[i-1] != r:
            flag = True
            break
    if flag:
        print('B')
    else:
        print(arr[n-1] * r)
else:
    # 일반항 검사 전에 0으로 나누는 경우 방지
    if arr[1] - arr[0] == 0:
        print('B')
        exit()
    
    # 나눗셈이 정확히 떨어지는지 확인
    if (arr[2] - arr[1]) % (arr[1] - arr[0]) != 0:
        print('B')
        exit()
    
    a = (arr[2] - arr[1]) // (arr[1] - arr[0])
    b = arr[1] - arr[0] * a  # 직접 계산
    
    flag = False
    for i in range(1, n):
        if arr[i] != arr[i-1] * a + b:
            flag = True
            break
    
    if flag:
        print('B')
    else:
        print(arr[n-1] * a + b)
