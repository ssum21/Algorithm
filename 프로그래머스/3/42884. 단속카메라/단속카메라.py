def solution(routes):
    routes.sort(key = lambda x:x[1])
    
    camera = -30001
    count = 0
    
    for s, e in routes:
        if camera < s:
            count += 1
            camera = e
    
    return count
