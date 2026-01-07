import sys
input = sys.stdin.readline

num_switch = int(input())
switch_states = list(map(int, input().split()))
case = int(input().strip())
for i in range(case):
    gender, position = map(int, input().split())
    if gender == 1:
        for j in range(position - 1, num_switch, position):
            switch_states[j] = (switch_states[j] + 1) % 2
    else:
        left = position - 2
        right = position
        switch_states[position - 1] = (switch_states[position - 1] + 1) % 2
        while left >= 0 and right < num_switch:
            if switch_states[left] == switch_states[right]:
                switch_states[left] = (switch_states[left] + 1) % 2
                switch_states[right] = (switch_states[right] + 1) % 2
                left -= 1
                right += 1
            else:
                break
for i in range(num_switch):
    print(switch_states[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
    