# https://school.programmers.co.kr/learn/courses/30/lessons/60058
# 문제해석 
    # - u,v로 쪼갤 때, u는 올바른 괄호 문자열일 때 쪼개면 된다
    # u : 균형잡힌 괄호 문자열, v : 나머지
# 스택사용
# 재귀

def devide(p): # 문자열 p를 u와 v로 분리
    # u : 균형잡힌 괄호 문자열, v : 나머지
    open_p, close_p = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i+1], p[i+1:] # u, v

def isBalanced(u): # 문자열 u가 올바른 괄호 문자열인지 체크
    stack = []
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    # 1
    if not p: 
        return ""
    
    # 2
    u, v = devide(p) 
    
    # 3
    if isBalanced(u): 
        return u + solution(v)
    # 4
    else: 
        answer = '('            # 4-1
        answer += solution(v)   # 4-2
        answer += ')'           # 4-3
        
        for p in u[1:len(u)-1]: # 4-4
            if p == '(':
                answer += ')'
            else:
                answer += '('
    # 4-5
    return answer 
    