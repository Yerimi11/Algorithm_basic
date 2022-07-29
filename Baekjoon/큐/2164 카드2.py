# 데크로 해결
# N이 최대 50만이지만, 데크로 삽입 삭제 시 O(1) 상수시간만큼의 시간복잡도가 들기 때문에 문제가 발생하지 않는다.

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
num_li = list(range(1, n+1))

dq = deque(num_li)

while len(dq) >= 0:
    if len(dq) == 1:
        print(dq[0])
        break
    dq.popleft()
    dq.append(dq.popleft())
