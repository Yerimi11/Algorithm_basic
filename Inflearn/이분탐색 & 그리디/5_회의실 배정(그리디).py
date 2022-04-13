import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

# 회의가 빨리 끝나야 더 많은 회의를 진행할 수 있으니, 정렬을 시작시간이 아닌 끝나는 시간을 기준으로 해야한다.
lst.sort(key=lambda x : (x[1], x[0]))   # 튜플에서 두번째를 기준으로 정렬

endtime = cnt = 0
for s, e in lst:
    print(s, e)
    if s >= endtime:
        endtime = e
        cnt += 1
print(cnt)

# count = []
# cnt = 1
# s, e = 0, 1
# temp = s
# while s < n and e != n:
#     print(lst.index(lst[s]), lst[s])
#     print(lst.index(lst[e]), lst[e])
#     print("------------")
#     if lst[s][1] <= lst[e][0]:
#         cnt += 1
#         s = e 
#         e = s + 1
#     else:
#         e = e + 1
#     if e == n:  # 첫 회의 시작 시간을 다음 케이스로 초기화
#         count.append(cnt)
#         if lst[s][0] != lst[temp][0]:
#             cnt = 1
#             temp = temp + 1
#             s, e = temp, temp + 1
#         else:
#             e = s + 1

# print(max(count))



# 5
# 1 4
# 2 3
# 3 5
# 4 6
# 5 7
# => 3

# 20
# 18 19
# 2 20
# 4 21
# 2 22
# 12 15
# 12 23
# 2 8
# 5 20
# 22 23
# 1 5
# 13 21
# 16 20
# 9 19
# 5 9
# 14 20
# 16 22
# 11 12
# 4 16
# 21 23
# 11 13
# => 8