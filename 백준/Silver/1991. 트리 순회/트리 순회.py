import sys
import math
from collections import deque
from collections import defaultdict

input=sys.stdin.readline

n = int(input())
tree = defaultdict(list)

for i in range(n):
    node, left, right = map(str, input().split())
    tree[node].append(left)
    tree[node].append(right)

def preorder(i):
    if(tree[i] == '.'):
        return
    elif(tree[i]):
        print(i, end='')
        preorder(tree[i][0])
        preorder(tree[i][1])
    else:
        return

def midorder(i):
    if(tree[i] == '.'):
        return
    elif(tree[i]):
        midorder(tree[i][0])
        print(i, end='')
        midorder(tree[i][1])
    else:
        return



def lastorder(i):
    if(tree[i] == '.'):
        return
    elif(tree[i]):
        lastorder(tree[i][0])
        lastorder(tree[i][1])
        print(i, end='')
    else:
        return

preorder('A')
print()
midorder('A')
print()
lastorder('A')
