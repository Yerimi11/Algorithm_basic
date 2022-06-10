def solution(s):
    # isdecimal 사용해서 숫자와 문자 구분,
    # 해쉬테이블(딕셔너리)로 {one:1} 식으로 저장
    # str = ""해서 숫자 추가해준다
    dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    num = ""
    eng = ""
    for x in s:
        if x.isdecimal() == True:
            num += x
            if eng in dict:
                num += dict[eng]     
                eng = ""
        else:
            eng += x    
        print("num : ", num)
        print("eng : ", eng)
        if eng in dict:
            num += str(dict[eng])
            eng = ""

    return int(num)

# enumerate로 푸는 방법도 해보자