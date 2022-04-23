# M : 0부터 시작
import sys
from collections import deque
# sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/6. 응급실/in1.txt", 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]
dq = deque(lst)
# targetIdx = m
count = 0

while dq:
    # if dq[targetIdx] != lst[m]:
    #     break
    maxN = max(dq)
    if dq[m] <= maxN:
        while maxN != dq[0]:
            dq.append(dq.popleft())
            # targetIdx -= 1
        # if targetIdx < 0:
            # targetIdx += len(dq)
        dq.popleft()
        # targetIdx -= 1
        count += 1
    else:
        while maxN != dq[0]:
            dq.append(dq.popleft())
        dq.popleft()
        count += 1
        break

print(count)

# 6 0
# 60 60 90 60 60 60
# ->5

# 5 2
# 60 50 70 80 90
# ->3