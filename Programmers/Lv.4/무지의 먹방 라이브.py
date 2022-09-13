# https://www.youtube.com/watch?v=zpz8SMzwiHM
from operator import itemgetter

def solution(food_times, k):
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i+1))
    foods.sort()
    
    before_time = 0
    for i, food in enumerate(foods):
        height = food[0] - before_time
        if height != 0:
            spend_time = height * n
            if spend_time <= k:
                k -= spend_time
                before_time = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key = itemgetter(1))
                return sublist[k]     [1]           
        n -= 1
    return -1


# def solution(food_times, k):
#     times = {}
#     for i, time in enumerate(food_times):
#         times[i+1] = time
#     now = 0
#     i = 1
#     while k >= now:
#         if i > len(food_times):
#             i = 1
#         if k == now:
#             break
#         else:
#             if times[i] == 0:
#                 i += 1
#             if times[i] > 0:
#                 times[i] -= 1
#             now += 1
#             i += 1
            
#     return i

solution([3,1,2], 5)