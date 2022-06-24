def solution(s):
    answer = 2147000000
    for n in range(1, len(s)//2+2):
        res = ""
        cnt = 1
        temp = s[:n]

        for i in range(n, len(s)+n, n):
            if temp == s[i:i+n]:
                cnt += 1
            else:
                if cnt == 1:
                    res += temp
                else:
                    res += str(cnt) + temp
                temp = s[i:i+n]
                cnt = 1
        answer = min(answer, len(res))
    return answer


# def solution(s):
#     # 반복되는 문자열을 압축한 후의 총 길이가 가장 작을 때의 길이를 리턴
#     # 스택에 차례대로 넣다가, 스택[0]과 같은 문자가 발견되면 append하기 전에

#     # 스택 길이로 저장하며 체크하지 말고, 최대길이 1부터 1씩 증가하며 쭉 찾아보고 최종 길이 min을 갱신
    
#     mlen = 2147000000
#     cnt = 0
#     while cnt <= len(s):
#         for i in range(len(s)//2+1):
#             result = ""
#             stack = []
#             cut = 0
#             cut_temp = ""
#             cnt += 1
#             in_stack = ""
#             ss = s[i:]
#             for x in ss:        
#                 stack.append(x)        
#                 if cnt == 1:
#                     in_stack = x
#                     temp = x # 비교용 문자
#                 else:
#                     in_stack = ''.join(stack[0:cnt+1])
#                     temp = ss[i-1:cnt]
#                     stack.pop(0)
#                 if in_stack == temp:
#                     if cnt > 1 :
#                         cut += 1
#                         cut_temp = in_stack
#                         stack = []
#                     else:
#                         result += x
#                 else:
#                     if cut > 1:
#                         result += str(cut)
#                         cut = 0
#                         result += cut_temp

                    
#             mlen = min(mlen, len(result))

#     print(mlen)
#     return mlen



solution("ababcdcdababcdcd") # 9
# solution("abcabcdede") # 8
# solution("abcabcabcabcdededededede") # 14
# solution("xababcdcdababcdcd") # 17
