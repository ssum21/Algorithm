import heapq
from collections import deque

def solution(jobs):
    jobs.sort(key= lambda x:(x[0], x[1]))
    index_jobs=deque()
    for i in range(len(jobs)):
        index_jobs.append((jobs[i][0], jobs[i][1], i))
    heap = []
    time = 0
    total_time = 0
    count = 0
    i=0
    time_limit = 1001
    N = len(jobs)
    while count < N:
        # 현재 시간에 도착한 모든 작업을 heap에 추가합니다.
        while index_jobs and index_jobs[0][0] <= time:
            s, l ,i = index_jobs.popleft()
            heapq.heappush(heap, (l, s))
        if heap:
            l, s = heapq.heappop(heap)
            count += 1
            time += l
            total_time += time - s
        else:
            # 작업이 아직 도착하지 않은 경우, 다음 작업의 시작시간으로 점프합니다.
            if index_jobs:
                time = index_jobs[0][0]
    return total_time // N

    return answer