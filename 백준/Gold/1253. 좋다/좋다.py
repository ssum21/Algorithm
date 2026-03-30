import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations
from functools import lru_cache
from typing import List, Optional

def solve():
    # 입력 처리
    n = int(input())
    arr = list(map(int, input().split()))
    # 풀이 작성
    arr.sort()
    total = 0
    if(n==1 or n==2):
        print(total)
    else:
        for i in range(n):
            left = 0
            right = n-1
            goal = arr[i]
            while (left<right):
                if(arr[left]+arr[right]==goal):
                    if(left!=i and right!=i):
                        total+=1
                        break
                    elif (left==i):
                        left+=1
                    else:
                        right-=1
                elif(arr[left]+arr[right]>goal):
                    right-=1
                else:
                    left+=1
        print(total)
        
if __name__ == "__main__":
    solve()
