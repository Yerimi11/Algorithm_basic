class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        
        def dfs(index, char):
            if len(char) == len(digits):
                result.append(char)
                return
        
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, char+j)
                
        if not digits:
            return []
        
        dfs(0, "")
        
        return result

# index 파라미터 사용 안하고 좀 더 깔끔한 코드    
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
#         answer = []
        
#         def combi(index, discovered=""):
#             if len(discovered) == len(digits):
#                 if digits:
#                     answer.append(discovered)
#                 return
#             for i in dic[digits[index]]:
#                 combi(index+1, discovered + i)

#         combi(0)
#         return answer

# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
#         if len(digits) == 0: return []
#         return [a+b for a in self.letterCombinations(digits[:-1]) for b in self.letterCombinations(digits[-1])] or list(dict[digits])
#         # return 앞에께 빈리스트(None)일 때 or 뒤 return된다
        
#         # for a in self.letterCombinations(digits[:-1]) -> '234'일때 슬라이싱 : '23'
#         # list유형이라서 a => 3:def, 2:abc로 가져옴
        
#             # for b in self.letterCombinations(digits[-1]) -> '234'일때 슬라이싱 :'4'
#                 # a+b
#         # or list(dict[digits]) # len(digits) == 1일때!
        