import sys

input = sys.stdin.readline

n, m = map(int, input().split())

height = 0
length = n

while length != 0:
    length //= 2
    height += 1

tree_size = pow(2, height+1)
tree_start_index = pow(2, height) - 1
tree = [sys.maxsize] * (tree_size+1)

for i in range(n):
    tree[tree_start_index+i+1] = int(input())

temp = n + tree_start_index

while temp != 1:
    tree[temp//2] = min(tree[temp//2], tree[temp])
    temp-=1

def find_tree(a,b):
    result = sys.maxsize
    while a<=b:
        if (a%2==1):
            result = min(result, tree[a])
            a+=1
        if (b%2==0):
            result = min(result, tree[b])
            b-=1
        a //= 2
        b //= 2
    return result

for _ in range(m):
    s_i, e_i = map(int, input().split())
    s_i += tree_start_index
    e_i += tree_start_index
    print(find_tree(s_i, e_i))
