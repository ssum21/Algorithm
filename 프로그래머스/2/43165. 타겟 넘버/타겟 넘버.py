from collections import defaultdict

def solution(numbers, target):
    tree = defaultdict(list)
    tree[0].append(numbers[0])
    tree[0].append((-1)*numbers[0])
    for i in range(1, len(numbers)):
        for j in tree[i-1]:
            tree[i].append(j+numbers[i])
            tree[i].append(j-numbers[i])
    answer = tree[len(numbers)-1].count(target)
    return answer