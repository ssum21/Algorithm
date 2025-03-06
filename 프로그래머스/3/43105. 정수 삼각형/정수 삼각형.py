def solution(triangle):
    tree_height = len(triangle)
    for i in range(1, tree_height):
        for j in range(i+1):
            if(j==0):
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            elif(j==i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
        
    answer = max(map(max, triangle))
    return answer