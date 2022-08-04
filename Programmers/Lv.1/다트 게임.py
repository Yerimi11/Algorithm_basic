def solution(dartResult):
    # nums = [0,1,2,3,4,5,6,7,8,9,10]
    answer = 0
    shots = [0 for _ in range(3)]
    i = -1
    for score in dartResult:
        if score.isdigit():
            # 10 판별?
            if score == '0' and shots[i] == 1:
                shots[i] = 10
                i -= 1
            i += 1
            shots[i] += int(score)
        
        else:
            if score == "S":
                shots[i] = shots[i]**1
            elif score == "D":
                shots[i] = shots[i]**2
            elif score == "T":
                shots[i] = shots[i]**3
            
            # print("shots[i]", shots[i])
            
            if score == "*":
                if i > 0:
                    shots[i-1] = shots[i-1]*2
                shots[i] = shots[i]*2
            elif score == "#":
                shots[i] = shots[i] * (-1)
        
        
    answer = sum(shots)
    print("shots = ", shots)
        
    return answer

solution("10S")