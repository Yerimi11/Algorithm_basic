def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        # if signs[i] == True:
        if signs[i]:
            sum += absolutes[i]
        else:
            sum -= absolutes[i]
    return sum

# solution([4,7,12], [True, False, True])
