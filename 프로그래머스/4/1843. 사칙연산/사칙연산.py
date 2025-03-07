import sys

def solution(arr):
    num = []
    odd = []
    for i in range(0, len(arr), 2):
        num.append(int(arr[i]))
    for i in range(1, len(arr), 2):
        odd.append(arr[i])

    num_len = len(num)
    dp_max = [[-sys.maxsize] * (num_len) for _ in range(num_len) ]
    dp_min = [[sys.maxsize] * (num_len) for _ in range(num_len) ]
    
    for i in range(num_len):
        dp_max[i][i] = num[i]
        dp_min[i][i] = num[i]
                   
    for l in range(2, num_len+1):
        for i in range(num_len-l+1):
            j = i + l -1
            for k in range(i, j):
                if odd[k] == '+':
                   dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                   dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                else:
                   dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
                   dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])
    return dp_max[0][num_len-1]