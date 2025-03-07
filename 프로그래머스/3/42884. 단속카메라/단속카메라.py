def solution(routes):
    # 종료 지점을 기준으로 정렬합니다.
    routes.sort(key=lambda x: x[1])
    
    count = 0      # 설치한 카메라 수
    camera = -30001  # 초기 카메라 위치 (최소 진입 지점보다 작은 값으로 설정)
    
    for s, e in routes:
        # 현재 차량의 진입 지점이 현재 카메라 위치보다 크다면,
        # 현재 카메라로 커버할 수 없으므로, 새로운 카메라를 해당 차량의 진출 지점에 설치합니다.
        if s > camera:
            count += 1
            camera = e
            
    return count
