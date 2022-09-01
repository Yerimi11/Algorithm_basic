def solution(s):
    # check = {')':'('}
    stack1 = [] # s를 담을 stack
    stack2 = [] # '짝을 못 찾은 )'
    for x in s: 
        stack1.append(x)
    
    if stack1[0] == ')': # )()() 의 경우
        return False
    
    while stack1:
        x = stack1.pop()
        if x == ')':
            if stack1[-1] == '(':
                stack1.pop()
            else: # stack1[-1] == ')':
                stack2.append(x)
        else:
            if stack2:
                stack2.pop()
            else: # s의 마지막 원소가 '('라면 바로 False
                return False

    return True

# ((() # s
# ))   # stack