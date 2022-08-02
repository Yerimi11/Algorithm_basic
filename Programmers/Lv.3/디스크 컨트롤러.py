# 설명해볼 수 있나요?

import heapq

def solution(jobs):
    worktime_sum, worktime, jobs_idx = 0, 0, 0 # worktime: 작업 시점
    start_work = -1 
    heap = []
    
    while jobs_idx < len(jobs): # jobs를 전부 탐색할 때 까지
        for job in jobs:
            # 현재 시점(시간)에서 처리할 수 있는 job을 heap에 저장
            if start_work < job[0] <= worktime:
                # 작업소요시간(job[1])을 기준으로 우선순위 큐 정렬
                heapq.heappush(heap, [job[1], job[0]])
        
        # 처리할 job이 있는 경우
        if len(heap) > 0: 
            curr = heapq.heappop(heap)
            start_work = worktime
            worktime += curr[0] # 작업소요시간
            # 총 작업 시간 합계 = 종료시간 - 작업 요청 시간
            worktime_sum += worktime - curr[1] 
            jobs_idx +=1
        else: # 처리할 작업이 없는 경우 다음 시점(시간)으로 넘어감
            worktime += 1
                
    return worktime_sum // len(jobs)

solution([[0, 3], [1, 9], [2, 6]]) # 9