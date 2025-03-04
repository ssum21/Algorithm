import sys

input = sys.stdin.readline

n, m, k = map(int, input().split()) #수의 개수, 변경 횟수, 곱 구하는 횟수

length = n
height = 0
MOD = 1000000007

while length!=0:
    length //= 2
    height += 1

tree_size = pow(2, height + 1)
start_tree_left_index = pow(2, height) - 1
tree = [1] * (tree_size + 1)

for i in range(start_tree_left_index+1, start_tree_left_index+ n+1):
    tree[i] = int(input())

temp = tree_size

while temp != 1:
    tree[temp//2] = tree[temp//2] * tree[temp] % MOD
    temp -= 1

def change_val(index, value):
    tree[index] = value
    while index > 1:
        index //= 2
        tree[index] = tree[index*2] % MOD * tree[index*2+1] %MOD 

def mux(s, e):
    result = 1
    while s<=e:
        if s%2==1:
            result = tree[s] * result % MOD
            s+=1
        if e%2==0:
            result = tree[e] * result % MOD
            e-=1
        s //= 2
        e //= 2
    return result


for i in range(m+k):
    mode, s, e = map(int, input().split())
    s += start_tree_left_index
    if (mode == 1):
        change_val(s, e)
    else:
        e += start_tree_left_index
        print(mux(s, e))
