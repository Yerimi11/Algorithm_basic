def solution(new_id):

    # 1
    new_id = new_id.lower()

    # 2
    id = ''
    for x in new_id:
        if x.islower() == True:
            id += x
        if x.isdecimal() == True:
            id += x
        if x == '-' or x == '_' or x == '.':
            id += x
    
    # 3
    temp = []
    for x in id:
        if len(temp) == 0:
            temp.append(x)
        else:
            if temp[-1] == '.' and x == '.':
                temp.pop()
            temp.append(x)
    
    # 4
    if len(temp) >= 1 and temp[0] == '.':
        temp.pop(0)
    if len(temp) >= 1 and temp[-1] == '.':
        temp.pop()
    
    # 5
    if len(temp) == 0:
        temp.append('a')

    # 6
    while len(temp) >= 16:
        temp.pop()
        if len(temp) == 15:
            if temp[-1] == '.':
                temp.pop()
            break

    # 7
    while 0 < len(temp) <= 2:
        if len(temp) == 3:
            break
        temp.append(temp[-1])
    # 끝자리가 . 이면 반복 못할 것임

    # finish
    answer = ''
    for x in temp:
        answer += x

    return answer
