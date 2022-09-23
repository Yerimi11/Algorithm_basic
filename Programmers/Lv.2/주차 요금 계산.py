def cal_minutes(records[i]):
    records[i][1] # 같은 차량일 때
    records[i][0], split(:) # 시, 분으로 쪼갬
        records[i][2] # 입차, 출차 구분
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
    parking_m = cal_minutes(records[i])
    if parking_m >= 180:
        pay += 5000
    parking_m -= 180
    parking_m /= 10 # 추가 단위 시간
    pay += (600 * parking_m) # 추가 단위 요금 계산
    
    return 