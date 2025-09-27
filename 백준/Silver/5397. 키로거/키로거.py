import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    left_stack = []
    right_stack = []
    input_str = sys.stdin.readline().strip()

    for char in input_str:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)

    left_stack.extend(reversed(right_stack))
    
    print(''.join(left_stack))