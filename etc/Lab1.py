def solution(p, s):
    sum = 0
    # 역/정방향 둘 다 계산해보고 더 적은 횟수로 채택
    for i in range(len(p)):
        a = abs(int(p[i])-int(s[i]))  # 정방향
        b = abs(10-a)       # 역방향
        sum += min(a, b)
    print(sum)
    return sum

solution("82195", "64723") # 13
solution("00000000000000000000", "91919191919191919191") # 20
