import sys

input = sys.stdin.readline

result = [] #숫자들 스택
calc_stack = [] #연산기호 스택

arr = list(map(str, input().strip()))

precedence = {'+' : 1, '-': 1, '*' : 2, '/' : 2}

for index in arr:
    if index.isalpha():
        result.append(index)
    elif index == '(':
        calc_stack.append(index)
    elif index == ')':
        while calc_stack and calc_stack[-1]!='(':
            result.append(calc_stack.pop())
        calc_stack.pop()
    else:
        while calc_stack and calc_stack[-1]!='(' and precedence[index] <= precedence[calc_stack[-1]]  :
            result.append(calc_stack.pop())
        calc_stack.append(index)

while calc_stack:
    result.append(calc_stack.pop())

print(''.join(result))