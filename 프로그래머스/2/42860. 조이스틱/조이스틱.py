def solution(name):
    def vertical(char):
        diff = ord(char) - ord('A')  
        return min(diff, 26 - diff)
    
    total_vertical = sum(vertical(i) for i in name)
    min_move=1001
    len_name=len(name)
    min_horizon=len_name- 1
    for i in range(len_name):
        cumu = i + 1
        while cumu < len_name and name[cumu] == 'A':
            cumu +=1
        move = min (2*(len_name-cumu)+i, min_horizon, 2*i+(len_name-cumu))
        min_move = min(min_move , move)
    
    return min_move + total_vertical