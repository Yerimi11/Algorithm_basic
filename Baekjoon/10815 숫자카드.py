import sys
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

n_list.sort()
answer = []

for m in m_list:
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2

        if n_list[mid] == m:
            answer.append(1)
            break
        elif n_list[mid] > m:
            right = mid - 1
        else:
            left = mid + 1
    
    if left > right:
        answer.append(0)


print(*answer)
