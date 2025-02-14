def solution(name):
    # 우선, 각 문자를 'A'에서 해당 문자로 만드는 데 필요한 상하 이동 횟수 누적
    def vertical_moves(c):
        # 'A' ~ 'Z'를 숫자로 환산(0 ~ 25)
        diff = ord(c) - ord('A')  
        # ▲로만 가는 방법 vs ▼를 통해 뒤로 돌아가는 방법
        return min(diff, 26 - diff)
    
    n = len(name)
    
    # 1) 상하 이동 총합
    total_vertical = sum(vertical_moves(c) for c in name)

    # 2) 좌우 이동 최소 횟수(기본값: 그냥 끝까지 오른쪽 이동하는 경우)
    #    → (n - 1)번 이동
    min_horizontal = n - 1
    
    # 3) A 연속 구간을 어떻게 스킵할지 시뮬레이션
    for i in range(n):
        # 다음 문자가 'A'인 동안 j 증가
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1
        
        # 1) 오른쪽으로 i번 간 뒤, 왼쪽으로 돌아가기 (n - j) 
        #    즉, (i + (n - j)) 이 이동인데,
        #    왼쪽으로 돌아가는 과정에서 이미 i까지 이동한 것(i) 때문에
        #    "왕복"이 되는 경우 주의 => 2*i + (n - j)
        #    혹은 i + 2*(n - j)가 될 수도 있어,
        #    "처음부터 왼쪽" vs "오른쪽으로 갔다가 다시 왼쪽" 둘 다 고려해야 한다.
        # 일반적으로 조이스틱 문제 공식 풀이에서:
        #
        #  min( 2*i + (n - j),   i + 2*(n - j) )  
        #
        # 형태로 두 케이스를 비교해서 더 작은 것을 취한다.
        left_then_right = 2 * i + (n - j)
        right_then_left = i + 2 * (n - j)
        best_case = min(left_then_right, right_then_left)

        min_horizontal = min(min_horizontal, best_case)
    
    # 최종 결과 = 상하 이동 총합 + 위에서 구한 최소 좌우 이동
    return total_vertical + min_horizontal

