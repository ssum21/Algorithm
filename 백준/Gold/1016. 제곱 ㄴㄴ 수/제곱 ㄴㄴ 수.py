import math
import sys

input = sys.stdin.readline

min, max = map(int, input().split())

arr = [False] * (max-min+1)

for i in range(2, int(math.sqrt(max)+1)):
    pow = i * i
    start_index = int(min / pow) # 제곱수가 아닌 수 -> 제곱수는 무언가를 곱해서 만드는 수 ? 인걸로 이해했는데
    if min % pow!=0:
        start_index += 1
    for j in range(start_index, int(max/pow)+1):
        arr[int((j*pow) - min)] = True

count = 0
for i in range(0, max-min+1):
    if arr[i] == False:
        count += 1

print(count)
