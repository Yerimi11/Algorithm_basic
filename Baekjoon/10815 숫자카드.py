import sys
from tracemalloc import start
from unittest.util import _MIN_DIFF_LEN
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# 이분탐색
# 반씩 줄여가는거.
# start, end, mid, target

# 네번째줄에 있는 숫자가 두번째 줄에 있으면 1 없으면 0
# 먼저 정렬부터 하고 이분탐색을 어떻게 적용할지?

# 두번째, 네번째 카드들을 정렬하면
# -10 2 3 6 10
# -10 -5 2 3 4 5 9 10
# 여기서 어느쪽을 이분탐색하지? 

n_list = sorted(n_list)
m_list = sorted(m_list)
answer = []

start_index, end_index = 0, len(n_list)-1
for m in m_list:
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2

        if n_list[mid_index] == m:
            answer += 1
            break
        elif n_list[mid_index] < m:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
            answer += 0

    print(answer)
