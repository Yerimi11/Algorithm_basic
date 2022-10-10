import sys
input = sys.stdin.readline

def binary(num, target):
    left, right = 0, n-1

    while left <= right:
        mid = (left+right) // 2
        if num[mid] == target:
            return 1
        elif num[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0


n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

answer = []
for i in range(len(m_list)):
    answer.append(binary(n_list, m_list[i])) # 출력방식 한 줄로 수정할 것

print(*answer)
