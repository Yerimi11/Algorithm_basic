# 50m (구상 23m+코드구현 27m)
# https://school.programmers.co.kr/learn/courses/30/lessons/42888

from collections import deque
def solution(record):
    result = []
    userID = {}
    status_list = deque()
    message = {'Enter':'님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for x in record:
        x = x.split()
        if len(x) == 2:
            status, uid = x[0], x[1]    
        else:
            status, uid, nickname = x[0], x[1], x[2]
            if status == "Enter" or status == "Change":
                userID[uid] = nickname
        
        if status == "Enter" or status == "Leave":
            status_list.append((uid, status))

    # print("status_list: ", status_list)
    while status_list:
        text = ''
        uid, status = status_list.popleft()
        text += userID[uid] + message[status]
        result.append(text)
        # print(text)
    # print(result)
    return result