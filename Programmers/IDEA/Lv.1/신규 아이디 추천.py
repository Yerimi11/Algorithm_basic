def solution(new_id):
    answer = ''
    return answer


# 3단계 -> 스택을 사용해서, 스택[-1]과 ID[0]이 둘 다 '.'이면 하나 pop하기
# 혹은 for문으로 문자 하나씩 보면서 마지막에 temp에 넣고, 다음 루프를 돌 때 if 문자 == '.'이면 temp도 '.'인지 체크 후 pop 처리 -> 다음 루프 돌 때 문제 없나?