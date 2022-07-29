# 중간 값을 기준으로 나눈 left_heap, right_heap 두 힙이 필요하다.
# 짝수개 일 때 두 수 중 작은 수를 출력해야하기 때문에, 중간값은 left_heap의 루트 위치에 들어가게 된다.
# 삽입할 때마다 최대 힙의 최댓값, 최소 힙의 최솟값을 비교해서 안맞다 싶으면 두개 위치 바꾸기
# 입력 갯수가 홀수면 최소 힙의 루트를 출력
# 입력 갯수가 짝수면 각 힙의 루트를 비교해서 더 작은놈 출력

import sys
import heapq

input = sys.stdin.readline

n = int(input())

# 최대 힙, 최소 힙 구현
left_heap = []
right_heap = []

for i in range(1, n+1):
    num = int(input())

    # i가 홀수면 최소 힙에, 짝수면 최대 힙에 삽입
    if i % 2 != 0:
        heapq.heappush(right_heap, [num, num])
    else:
        heapq.heappush(left_heap, [-num, num])

    # 삽입할 때마다 최대 힙의 최댓값, 최소 힙의 최솟값을 비교해서 안맞다 싶으면 두개 위치 바꾸기
    if right_heap and left_heap:
        if right_heap[0][1] < left_heap[0][1]: #최소힙의 루트노트가 최대힙의 루트노드보다 작으면
            maximum = heapq.heappop(left_heap)
            maximum[0] = -maximum[0]
            minimum = heapq.heappop(right_heap)
            minimum[0] = -minimum[0]

            # 두 루트노드를 자리 바꾸기
            heapq.heappush(right_heap, maximum)
            heapq.heappush(left_heap, minimum)
    
    # 입력 갯수가 홀수면 최소 힙의 루트를 출력
    if i % 2 != 0:
        print(right_heap[0][1])

    # 입력 갯수가 짝수면 각 힙의 루트를 비교해서 더 작은놈 출력
    else:
        if right_heap[0][1] > left_heap[0][1]:
            print(left_heap[0][1])
        else:
            print(right_heap[0][1])



# # 시간초과
# import heapq as hq
# import sys
# input = sys.stdin.readline
# n = int(input())
# li = []
# for i in range(n):
#     a = int(input())
#     hq.heappush(li, a)
#     li.sort()
#     if (len(li)%2) == 0:
#         print(li[(len(li)//2)-1])
#     else:
#         print(li[len(li)//2])

# 7
# 1
# 5
# 2
# 10
# -99
# 7
# 5