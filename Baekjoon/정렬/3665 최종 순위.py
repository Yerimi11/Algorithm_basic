# 3

# 5
# 5 4 3 2 1     # 앞에서부터 1등, 팀 번호
# 2
# 2 4
# 3 4

# 3
# 2 3 1
# 0

# 4
# 1 2 3 4
# 3
# 1 2
# 3 4
# 2 3

# 위상정렬
# 인접그래프 생성
# indgree 배열 생성

import sys
from collections import deque

N = int(sys.stdin.readline())
for _ in range(N):
    n = int(sys.stdin.readline())
    ranking = list(map(int, sys.stdin.readline().split()))

    queue = deque()
    tree = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            tree[ranking[i]].append(ranking[j])
            indegree[ranking[j]] += 1

    m = int(sys.stdin.readline())
    for _ in range(m):
        up, down = map(int, sys.stdin.readline().split())
        check = True
        for i in tree[up]:
            if i == down:
                tree[up].remove(down)
                tree[down].append(up)
                indegree[down] -= 1
                indegree[up] += 1
                check = False
        if check:
            tree[down].remove(up)
            tree[up].append(down)
            indegree[up] -= 1
            indegree[down] += 1

    for i in range(1, n + 1):
        if indegree[i] == 0: # 1등으로 되어 있는 팀 (자신에게 들어오는 방향인 간선 수가 0)
            queue.append(i)

    result = True
    result_list = []
    if not queue:
        result = False
    while queue:
        if len(queue) > 1:
            result = False
            break
        now = queue.popleft()
        result_list.append(now) # 현재 1등인 팀을 result_list에 넣는다
        for i in tree[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
            elif indegree[i] < 0:
                result = False
                break

    if not result or len(result_list) < n:
        print('IMPOSSIBLE')
    else:
        print(*result_list)
        
# 출처: https://ca.ramel.be/158 [MemoLOG:티스토리]