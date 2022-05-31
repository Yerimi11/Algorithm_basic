


def solution(N, stages):
    lv = len(stages)
    temp = 0
    result = []
    for i in range(N+1):
        notclear = 0
        for j in range(lv):
            if i == stages[j]:
                notclear += 1
        if lv-temp != 0:                    # solution(5, [3,3,3,3]) 일 때 실패하는 부분 해결
            fail = notclear / (lv-temp)
            temp += notclear
        else:
            fail = 0.0
        result.append(fail)

    # result idx 내림차순 정렬
    answer = []
    result[0] = -2147000000
    for i in range(1, N+1):
        answer.append((result.index(max(result))))
        result[answer[i-1]] = -2147000000

    print(answer)

# solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) # [3,4,2,1,5]
# solution(4, [4,4,4,4,4]) # [4,1,2,3]
solution(5, [3,3,3,3])
    # 모든 인원이 3단계에서 실패한 경우, 4,5 단계의 실패율은 0.0이 되야 하는데
    # 분모를 남은 유저 수 로 해놓은 경우 0/0 이 되버려서, Nan으로 값이 잡혀 계속 실패합니다.