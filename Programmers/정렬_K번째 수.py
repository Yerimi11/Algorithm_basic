def solution(array, commands):
    answer = []
    result = []
    
    for a in commands:
        i, j, k = a[0], a[1], a[2]
        answer = array[i-1:j]
        answer.sort()
        result.append(answer[k-1])
    return result