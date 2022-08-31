# 해시테이블로 {name: 1} 참가자 명단 저장하는데, key가 동명이인일 경우 value += 1
# 완주한 명단은 참가자 명단에서 key값 찾아 value -1 해준다
# 값이 0이 아닌 참가자의 key(이름)을 return 

from collections import defaultdict
def solution(participant, completion):
    answer = ''
    attendance = defaultdict(int)
    for name in participant:
        attendance[name] += 1
    
    for name in completion:
        attendance[name] -= 1
    
    for name, num in attendance.items():
        if attendance[name] > 0:
            answer += name
    return answer