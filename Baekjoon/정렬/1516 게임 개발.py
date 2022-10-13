# 입력 형식: (idx+1건물번호)를 짓는데 걸리는 시간, 선행으로 지어야하는 건물 번호, -1 (입력값 끝 표시)
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

# 노드와 간선의 정보 저장
building_nums = [[] for _ in range(N + 1)]
# 각 노드의 진입차수 저장
pre_build_cnt = [0] * (N + 1)
# 건물 짓는데 걸리는 시간
hour = [0] * (N + 1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))[:-1] # 마지막(-1)원소 직전까지만 슬라이싱
    hour[i] = data[0]
    pre_build_data = data[1:]

    # 간선 연결 및 진입차수 설정
    for j in pre_build_data:      # i번 건물을 지을 때
        building_nums[j].append(i)  # 선행 필요로 하는 건물 번호와 같은 idx에 i(지어질 건물 번호)를 기록
        pre_build_cnt[i] += 1       # 선행건물 갯수


# 위상 정렬 함수
def topology_sort():
    result = [0] * (N + 1)
    queue = deque()

    for i in range(1, N + 1):
        if pre_build_cnt[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        # 큐에서 꺼낸 노드 번호에 해당하는 건물을 짓는데 걸리는 시간 저장
        # 선수 건물 짓는데 걸리는 시간이 포함되어 있음!
        # 즉, '선수 건물 짓는데 걸리는 시간 + 현재 건물 짓는데 걸리는 시간'이 저장됨
        result[now] += hour[now]
        for b in building_nums[now]:
            pre_build_cnt[b] -= 1
            # b번호 건물을 짓기 전에 먼저 지어야하는 선수 건물 짓는데 걸리는 시간으로 갱신
            result[b] = max(result[b], result[now])
            if pre_build_cnt[b] == 0:
                queue.append(b)

    return result


answer = topology_sort()
for i in range(1, N + 1):
    print(answer[i])