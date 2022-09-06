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


# def solution(id_list, report, k):
#     # 유저아이디는 해쉬테이블(딕셔너리)로 {아이디:신고횟수} 구조로 만들어 놓자
#     dict = {}
#     for x in id_list:
#         dict[x] = 0
        
#     # report->set으로 동일 인물 동일 신고 제외
#     report = set(report)
    
#     # report[i].split()으로 분리 되는지, 되면 report[i][1]의 신고 수 += 1 카운팅 해줌(딕셔너리)
#     for i in report:
#         a, b = i.split()
#         dict[b] += 1
    
#     # 딕셔너리 value값이 k보다 큰 id를 result에 따로 저장한다.
#     result = []
    
#     for item in dict.items():
#         if item[1] >= k:
#             result.append(item[0])
    
#     answer = [0] * len(id_list)
#     for i in report:
#         a, b = i.split()
#         for name in result:
#             if name == b:
#                 answer[id_list.index(a)] += 1 # 여기서 시간복잡도 N^3 될 가능성 있음.
#     # 각 for문마다 반복 횟수가 전부 달라서 정확하게는 n^2라고 쓰는 건 잘못된거지만 
#     # 위의 (이중반복문 실행 횟수) * (id_list 길이) 이렇게 곱하기로 계산해야 함.
#     # 그리고 반복문 중에 하나가 result 길이만큼 반복을 도는데 
#     # result는 위에서 특정 조건에서 걸러져서 그 수가 줄어들 수는 있음. 
#     # 그런데 나머지 반복량을 책임지는 report나 id_list는 인풋값 그대로 받아와서 쓰는 거니까 
#     # 입력값이 엄청 많다면 엄청 많이 돌아야 될거임
#     return answer


# # 해시테이블의 시간복잡도는 O(1) ?


# solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
# # => [2,1,1,0]
