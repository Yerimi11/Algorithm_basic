import sys
input = sys.stdin.readline

# N장의 카드 중에 3장을 골라서
# 숫자 M과 가까운 3개의 숫자의 합을 만들어라
# 브루트포스, 완전탐색

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cards[i] + cards[j] + cards[k] > M:
                continue
            else:
                result = max(result, cards[i] + cards[j] + cards[k])

print(result)

# 3중 for문 시간복잡도 O(n^3)

# max(3개의 합) < M 
# 3포인터?

# num_sum = M
# result = []
# # print(sum(cards[-3:]))

# def nums_sum(start, mid, end, result):
#     num_sum = cards[start]+cards[mid]+cards[end]
#     if num_sum < M:
#         result.append(num_sum)
#         result = set(result)
#         return result

#     # while (num_sum != sum(cards[-3:])):
#     # while (cards[start] == cards[-3] and cards[mid] == cards[-2] and cards[end] == cards[-1]):
# while (cards[start] != cards[-3]): => for문으로 수정해보자. 브루트포스 문제니까 3중 for문이어도 상관 없다.
#     nums_sum(start+1, mid, end, result)

#     while (cards[mid] != cards[-2]): 
#         nums_sum(start, mid+1, end, result)

#         while (cards[end] != cards[-1]):    
#             nums_sum(start, mid, end+1, result)


# nums_sum(0, 1, 2, result)
# print(max(result))
# print(result)
 
