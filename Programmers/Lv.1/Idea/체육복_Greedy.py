# 여분(reserve)-j 2중 for문 돌려서(1-lost,2-reserve), 
# if j-1, j+1이 lost[i]랑 같으면
# lost.pop(i)하고
# return n-len(lost)
# -> 예시1처럼 빌려주는 케이스가 여러개여도 통과되나?

# 앞쪽에, 조건 추가(=전처리) : 여분 O 학생이 도난 당할 수도 있음
# if reserve[i] in lost:
    # reserve.pop(i)

# https://rain-bow.tistory.com/30