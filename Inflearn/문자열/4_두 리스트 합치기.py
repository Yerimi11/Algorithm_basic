import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# for i in m_list:
#     n_list.append(i)
# n_list.sort()
# print(n_list)

# sort는 O(NlogN) 이기 때문에, sort를 사용하지 않고 작성해볼 것!
# n_list의 원소와 m_list의 원소를 대소비교 후 new_list에 넣어 출력
new_list = []
p1 = p2 = 0
while p1 < n and p2 < m:
    if n_list[p1] <= m_list[p2]:
        new_list.append(n_list[p1])
        p1 += 1
    else:
        new_list.append(m_list[p2])
        p2 += 1

if p1 == n:
    new_list += m_list[p2:]
if p2 == m:
    new_list += n_list[p1:]
    
for i in new_list:
    print(i, end = ' ')

# 시간복잡도 -> O(N) : 리스트를 원소 N개만큼 탐색하므로.
# 더 정확히는, n개 원소를 가진 리스트랑 m개 원소 리스트를 합치는거니 O(N+M)