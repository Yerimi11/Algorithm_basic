def solution(id_list, report, k):
    SingoIds = set()
    answer = [0] * len(id_list)
    
    # 유저아이디를 해쉬 {아이디:신고횟수} 구조로 생성해 정리
    dict = {}
    for x in id_list:
        dict[x] = 0
        
    # report->set으로 동일 인물 동일 신고 우선 제외
    report = set(report)
    
    # report[i].split()으로 분리 후 report[i][1]의 신고 수 += 1 카운팅
    for x in report:
        userId, reportedId = x.split()
        dict[reportedId] += 1
    
    # 딕셔너리 value값이 k보다 큰 id를 SingoIds에 따로 저장한다. 
    # 신고 처리가 되어 정지당할 Id list
    for userId, nums in dict.items():
        if nums >= k:
            SingoIds.add(userId)
            
    # 각 유저별로 정지 처리 결과 메일을 받은 횟수를 배열에 담아 return
    for x in report:
        userId, reportedId = x.split()
        if reportedId in SingoIds: # SingoIds: set()이라 O(1)
            answer[id_list.index(userId)] += 1
    
    return answer

# 정규 표현식
import re
def solution(new_id):    
    #1단계 & 2단계 소문자 치환, 제거
    answer = re.sub('[^0-9a-z_.\-]+','',new_id.lower())
    
    #3단계 . 2번 이상을 1개로 압축
    answer = re.sub('\.\.+','.',answer)
    
    #4단계 양끝 . 제거
    answer = answer.strip('.')
    
    #5단계 빈문자열 a 추가
    if answer =='': answer='a'
        
    #6단계 15개제외하고 문자모두제거, 우측 . 제거
    answer = answer[:15].rstrip('.')
        
    #7단계 길이 3 될 때까지 끝 문자 추가    
    answer+=answer[-1]*(3-len(answer))
        
    return answer
