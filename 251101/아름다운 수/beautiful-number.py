n = int(input())

# Please write your code here.

answer = []
result = 0

def choose():
    global result

    if len(answer) == n:
        result += 1
        return
    
    if len(answer) > n:
        return

    for i in range(1, 5):
        answer.extend([i] * i)
        choose()
        for _ in range(i):
            answer.pop()

choose()
print(result)