import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, input().split(' ')))
arr.insert(0, 0)
tarr = [0] * (N+1)
num=0


def ms(s, e):
    global num
    if(e-s<1):
        return
    m = int(s + (e-s)/2)
    ms(s, m)
    ms(m+1, e)
    for i in range(s, e+1):
        tarr[i] = arr[i]
    k=s
    index1 = s
    index2 = m+1
    while index1<=m and index2 <=e :
        if tarr[index1] > tarr[index2]:
            arr[k]=tarr[index2]
            num = num + index2 - k
            k += 1
            index2+=1
        else:
            arr[k]=tarr[index1]
            k += 1
            index1 += 1
    while index1<=m:
        arr[k]=tarr[index1]
        k += 1
        index1 += 1
    while index2<=e:
        arr[k]=tarr[index2]
        k+=1
        index2+=1
    
ms(1, N)

print(num)

