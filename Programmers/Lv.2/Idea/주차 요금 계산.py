def cal_minutes(time, carnums, inout):
    # if carnums == 스택?: # 같은 차량일 때
    # 혹은 records를 맨뒤부터 탐색?
    
    # 차량번호를 key: [시간, inout내역]을 리스트형 value로 가지는 해쉬 만들기
    
    # 같은차량이어야하고, Out, In 데이터가 다 있을 때 계산됨
    # 추가로, if out 데이터가 없으면 23:59 출차로 간주하는 예외사항 필요
    h, m = time.split(:) # 시, 분으로 쪼갬
    if inout == 'IN':
        In_h, In_m = h, m
    else:
        Out_h, Out_m = h, m
        
    h_diff = Out_h - In_h
    h_to_m = h_diff * 60

    if Out_m < In_m:
        h_diff -= 1
        Out_m += 60
    if Out_m > In_m:
        m_diff = Out_m - In_m
        
    
    return h_to_m + m_diff

def solution(fees, records):
    pay = 0
    
    # records 문자열 파싱
    for i in range(len(records)):
        time, carnums, inout = records[i].split()
        parking_m = cal_minutes(time, carnums, inout)
        
    if parking_m >= 180:
        pay += 5000
    parking_m -= 180
    parking_m /= 10 # 추가 단위 시간
    pay += (600 * parking_m) # 추가 단위 요금 계산
    
    return 


# https://velog.io/@minnseong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%B0%A8-%EC%9A%94%EA%B8%88-%EA%B3%84%EC%82%B0