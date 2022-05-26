def ant(num):
    res = []
    char = temp = str_res = ''

    for i in range(len(num)):
        if i == 0:
            temp = num[i]
        elif num[i] == char:
            temp += num[i]
        else:
            res.append(temp)
            temp = num[i]
        char = num[i]
    res.append(temp)

    for x in res:
        str_res += (str(len(x)) + x[0])
    return str_res

def solution(n):
    ant_num = ""
    for i in range(n):
        if i == 0:
            ant_num = "1"
        else:
            ant_num = ant(ant_num)

    return ant_num[::-1]

# print(solution(5))