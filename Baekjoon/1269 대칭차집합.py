from collections import defaultdict
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = input().split()
B = input().split()

dict = defaultdict(int)
for i in A:
    dict[i] += 1
for i in B:
    dict[i] += 1

# print(dict)
count = 0
for num, cnt in dict.items():
    if cnt > 1:
        count += 1
print((len(A)-count)+(len(B)-count))



# # 시간초과
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# A = input().split()
# B = input().split()

# nums_A = []
# nums_B = []
# # 각 집합의 공통 원소를 빼고 남은 원소의 갯수들의 합을 구한다

# for a in A:
#     for b in B:
#         if a == b:
#             nums_A.append(a)
#             break

# for b in B:
#     for a in A:
#         if a == b:
#             nums_B.append(b)
#             break

# res = len(nums_A) + len(nums_B)
# print(res)
