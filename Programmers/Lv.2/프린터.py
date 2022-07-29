from collections import deque

def solution(priorities, location):
    dq = deque(priorities)
    idx = location
    cnt = 0
    while idx != -1:
        priority_doc = max(dq)
        if idx == 0:
            # 인쇄 대기목록 맨 앞의 문서가 우선순위로 출력될 문서가 아니면 마지막 순서로 보낸다
            if dq[0] != priority_doc:
                dq.append(dq.popleft())
                idx = len(dq)-1
            # 우선순위로 출력될 문서이면 몇 번째 출력인지 세고 바로 break
            else:
                cnt +=1
                break
        elif idx > 0:
            if dq[0] != priority_doc:
                dq.append(dq.popleft())
            else:
                dq.popleft()
                cnt += 1
            idx -= 1        
    return cnt