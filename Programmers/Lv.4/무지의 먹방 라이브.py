def solution(food_times, k):
    times = {}
    for i, time in enumerate(food_times):
        times[i+1] = time
    now = 0
    i = 1
    while k >= now:
        if i > len(food_times):
            i = 1
        if k == now:
            break
        else:
            if times[i] == 0:
                i += 1
            if times[i] > 0:
                times[i] -= 1
            now += 1
            i += 1
            
    return i

solution([3,1,2], 5)