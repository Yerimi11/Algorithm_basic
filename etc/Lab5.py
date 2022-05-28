res = 2147000000

def DFS(L, idx, nums, ch):
    global res
    if nums[idx] == 0:
        return
    if L >= len(nums)-1:
        return
    if idx == len(nums)-1:
        if res > L:
            res = L
        return
    else:
        if 0 <= idx < len(nums) and ch[idx] == 0:
            ch[idx] = 1
            DFS(L+1, idx+nums[idx], nums, ch)
            ch[idx] = 0
            DFS(L+1, idx-nums[idx], nums, ch)

def solution(nums):
    ch = [0] * len(nums)
    DFS(0, 0, nums, ch)
    print(res)
    return res



# 제출코드
# res = 2147000000

# def DFS(L, idx, nums):
#     global res
#     if L >= len(nums)-1:
#         return
#     if idx == len(nums)-1:
#         if res > L:
#             res = L
#         return
#     else:
#         if 0<= idx < len(nums):
#             DFS(L+1, idx+nums[idx], nums)
#             if nums[idx] == 0:
#                 return
#             DFS(L+1, idx-nums[idx], nums)
        

# def solution(nums):
#     DFS(0, 0, nums)
#     print(res)
#     return res





# from collections import deque

# def solution(nums):
#     dq = deque()
#     dq.append(0)
#     check = [-1] * len(nums)
#     cnt = 0
#     while dq:
#         now = dq.popleft()
        
#         if check[now] == -1:
#             cnt += 1
#             dq.append(now+nums[now])
#             check[now] = check[now] + 1 
#         else:
#             dq.append(now-temp)
#             cnt -= 1
#             check[now] = check[now] + 1
        
#         if now == len(nums) - 1:
#             return cnt
#             break
#         if nums[now] != 0:
#             temp = nums[now]

#     if check[len(nums) - 1] == -1:
#         return -1


solution([4, 1, 2, 3, 1, 0, 5])
