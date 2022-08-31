def combinationSum(candidates, target):
    result = []
    answer = []
    check = {}
    def dfs(depth, answer, target_sum):
        for i in candidates:
            answer.append(i)
            target_sum = sum(answer)
            if target < target_sum:
                answer.pop()
                return
            elif target == target_sum:
                if check[answer] == 1:
                    return
                else:
                    result.append(answer)
                    check[answer] = 1
                answer = []
            else:
                dfs(depth+1, answer, target_sum)
                answer.pop()
    
    dfs(0, answer, 0)
    return set(result)

combinationSum([2,3,6,7], 7)

# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         # candidates 숫자 횟수 제한 없이 더해서 target숫자 만들기
#         # 뺄셈으로 찾기 ! target - c
        
#         result = []
        
#         def dfs(csum, index, path):
#             if csum < 0:
#                 return
#             if csum == 0:
#                 result.append(path)
#                 return

#             for i in range(index, len(candidates)):
#                 dfs(csum - candidates[i], i, path + [candidates[i]])
        
#         dfs(target, 0, [])
#         return result

            