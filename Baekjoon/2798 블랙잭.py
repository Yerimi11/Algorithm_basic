(진행중)

import sys
input = sys.stdin.readline

# N장의 카드 중에 3장을 골라서
# 숫자 M과 가까운 3개의 숫자의 합을 만들어라

N, M = map(int, input().split())
cards = list(map(int, input().split()))

# max(3개의 합) < M  
# 3포인터?

num_sum = M
result = []
# # print(sum(cards[-3:]))

# def nums_sum(start, mid, end, result):
#     num_sum = cards[start]+cards[mid]+cards[end]
#     if num_sum < M:
#         result.append(num_sum)
#         result = set(result)
#         return result

#     # while (num_sum != sum(cards[-3:])):
#     # while (cards[start] == cards[-3] and cards[mid] == cards[-2] and cards[end] == cards[-1]):
# if (cards[start] != cards[-3]):
#     nums_sum(start+1, mid, end, result)

#     if (cards[mid] != cards[-2]):
#         nums_sum(start, mid+1, end, result)

#         if (cards[end] != cards[-1]):   
#             nums_sum(start, mid, end+1, result)


# nums_sum(0, 1, 2, result)
print(max(result)
# print(result)
