K, N = map(int, input().split())

# Please write your code here.
selected_nums = []

def print_permutation():
    for num in selected_nums:
        print(num, end = " ")
    print()

def find_permutations(cnt):
    if cnt == N:
        print_permutation()
        return

    for i in range(1, K+1):
        selected_nums.append(i)
        find_permutations(cnt + 1)
        selected_nums.pop()

find_permutations(0)