def solution(numbers, target):
    answer = 0
    def dfs(L, result):
        if L == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(L+1, result+numbers[L])
            dfs(L+1, result-numbers[L])
    dfs(0,0)
    return answer

solution([4, 1, 2, 1], 3)





