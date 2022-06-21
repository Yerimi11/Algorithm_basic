def solution(s):
    # 반복되는 문자열을 압축한 후의 총 길이가 가장 작을 때의 길이를 리턴
    # 스택에 차례대로 넣다가, 스택[0]과 같은 문자가 발견되면 append하기 전에

    # 스택 길이로 저장하며 체크하지 말고, 최대길이 1부터 1씩 증가하며 쭉 찾아보고 최종 길이 min을 갱신
    
    stack = []
    mlen = 2147000000
    cnt = 0
    result = []
    while cnt <= len(s):
        cnt += 1
        st = ""
        temp = s[0:cnt+1]
        for x in s:
            stack.append(x)
            st = ''.join(stack[0:cnt+1])
            if st == temp:
                result.append(st)
            else:
                continue
        mlen = min(mlen, len(result))

    print(mlen)
    return mlen



solution("ababcdcdababcdcd") # 9
# solution("abcabcdede") # 8
# solution("abcabcabcabcdededededede") # 14
# solution("xababcdcdababcdcd") # 17
