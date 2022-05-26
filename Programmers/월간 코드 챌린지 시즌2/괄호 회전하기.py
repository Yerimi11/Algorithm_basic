
def solution(s):
    dic = {')' : '(', ']' : '[', '}' : '{'}

    answer = 0
    for i in range(len(s)):
        stack = []
        ch = 0
        for x in s:
            if len(stack) == 0:
                if x in dic:
                    ch = 1
                    break
            
            if x in dic: # 닫힌 괄호이면
                if dic[x] != stack[-1]:
                    ch = 1
                    break
                stack.pop()
            else:        # 열린 괄호이면
                stack.append(x)

        if ch == 0 and len(stack) == 0:
            answer += 1
        
        s = s[1:] + s[0] # 문자열 회전
    # print(answer)
    return answer

solution("[](){}")
solution("}]()[{")
solution("[)(]")

    # 우선, 스택&큐&힙(팝)을 이용해 문자열 회전 기능을 먼저 구현한다.
    # 그 후, 올바른 괄호 문자열의 조건을 설정 후 갯수를 체크한다.
    # cnt = 0
    # a = []
    # for i in range(len(s)):
    #     a.append(s[i])
    
    # temp = []
    # for i in range(len(s)-1):
    #     # a.append(a.pop(0))  # 문자열 회전. 회전하기 전 처음 상태에서도 올바른지 체크해야 함!
    #     if a[i] == '(' or a[i] == '[' or a[i] == '{':    # 조건 설정 & 갯수 체크
    #         temp.append(a[i])
    #     else:
    #         if temp:
    #             if temp[0] == dic[i]:
    #                 temp.pop(0)
    #             else:
    #                 break


    #     print(a)


    # # print(cnt)
    # return cnt
