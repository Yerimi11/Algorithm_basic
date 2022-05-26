def solution(p, s):
    res = 0
    sum = 0
    for x, y in p, s:
        # for y in s:
            # 역/정방향 둘 다 계산해보고 더 적은 횟수로 채택
            x, y = int(x), int(y)
            a = abs(y-x)         # 정방향
            b = abs((x*10)-y)    # 역방향
            if a > b:
                sum += b
            else:
                sum += a
            pass

    print(sum)
    return res


solution("82195", "64723") # 13
# solution("00000000000000000000", "91919191919191919191") # 20