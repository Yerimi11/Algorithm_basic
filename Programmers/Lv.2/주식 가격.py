from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        sec = 0
        now_price = prices.popleft()

        for next_price in prices:
            sec += 1
            if next_price < now_price:
                break
        answer.append(sec)
    return answer

# def solution(prices):
#     length = len(prices)
#     answer = [i for i in range(length-1, -1, -1)]

#     stack = [0]
#     for i in range(1, length):
#         while stack and prices[stack[-1]] > prices[i]:
#             j = stack.pop()
#             answer[j] = i-j
#         stack.append(i)
#     return answer

# def solution(prices):
#     answer = [0]*len(prices)
#     stack = []
 
#     for idx, now_price in enumerate(prices):
#                         # 주식 가격이 떨어졌을 때 작동
#         while stack and now_price < prices[stack[-1]]:
#             top = stack.pop()
#             answer[top] = idx - top
#         stack.append(idx)
 
#     # for문 다 돌고 Stack에 남아있는 값들 pop
#     while stack:
#         x = stack.pop()
#         answer[x] = len(prices) - 1 - x
 
#     return answer

solution([1,2,3,2,3])