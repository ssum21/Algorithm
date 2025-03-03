import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) # 수의 개수, 변경 횟수, 구간 합 횟수

leafnodeV = n
height = 0

while leafnodeV!=0:
    leafnodeV//=2
    height+=1

tree = [0]*pow(2, height+1)
start_tree_index = pow(2, height) - 1
tree_size = pow(2, height+1)

for i in range(start_tree_index+1, start_tree_index+n+1):
    tree[i] = int(input())

temp = tree_size - 1

while temp!=1:
    tree[temp//2] += tree[temp]
    temp -= 1

def change_val(index, value):
    diff = value - tree[index]
    while(index > 0):
        tree[index] = tree[index] + diff
        index //= 2

def get_sum(s,e):
    partSum = 0
    while s<=e:
        if s%2==1:
            partSum += tree[s]
            s += 1
        if e%2==0:
            partSum+= tree[e]
            e -= 1
        s //= 2
        e //= 2
    return partSum

for _ in range(m+k):
    event, s, e = map(int, input().split())
    if event == 1:
        change_val(start_tree_index+s, e)
    else:
        s = start_tree_index + s
        e = start_tree_index + e
        print(get_sum(s, e))
