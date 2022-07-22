# 스코빌지수를 갱신시마다 heapq설정한 scoville 배열을 우선순위큐로 정렬 후,
# .heappop으로 새 값 계산하거나, .heappop()가 >= k이면 출력값 return

# Q. 제한사항에서 주의해야할 것은? - 우선순위큐로 해결 되나?
# - 시간복잡도 계산해보기!
# - n이 100만, 파이썬 1초에 1억회 연산이니 n^2은 X
# - 파이썬에서 리스트*정렬 => n*nlogn => n^2이라 X
# - nlogn일때, 100만*20 = 2000만 -> 1억회 연산에 영향 X
# - nlogn활용 : 힙, 퀵정렬, 머지소트

import heapq as hq

def solution(scoville, k):
    hq.heapify(scoville)
    cnt = 0
    while scoville:
        if scoville[0] >= k:
            return cnt
        else:
            temp = hq.heappop(scoville) + (hq.heappop(scoville)*2)
            hq.heappush(scoville, temp)
            cnt += 1
        if len(scoville) == 1 and scoville[0] < k:
            return -1


solution([1, 2, 3, 9, 10, 12], 7)