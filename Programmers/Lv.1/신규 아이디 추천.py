def solution(new_id):

    # 1
    new_id = new_id.lower()

    # 2
    id = ''
    for x in new_id:
        if x.islower() or x.isdecimal() or x == '-' or x == '_' or x == '.':
            id += x
    
    # 3 - 슬라이싱 이용도 될 것 같은데
    tempId = []
    for x in id:
        if len(tempId) == 0:
            tempId.append(x)
        else:
            if tempId[-1] == '.' and x == '.':
                tempId.pop()
            tempId.append(x)
    
    # 4 - if문을 합치거나, pop을 슬라이싱으로 바꾸면 일부 테케에서 틀린다. 왜지?
    if len(tempId) >= 1 and tempId[0] == '.':
        tempId.pop(0)
    if len(tempId) >= 1 and tempId[-1] == '.':
        tempId.pop()
    
    # 5
    if len(tempId) == 0:
        tempId.append('a')

    # 6
    while len(tempId) >= 16:
        tempId.pop()
        if len(tempId) == 15:
            if tempId[-1] == '.':
                tempId.pop()
            break

    # 7
    while 0 < len(tempId) <= 2:
        if len(tempId) == 3:
            break
        tempId.append(tempId[-1])

    # finish
    answer = ''
    for x in tempId:
        answer += x

    return answer