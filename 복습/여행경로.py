def solution(tickets):
    # 해쉬테이블로 정리
    airports = {}
    for ticket in tickets:
        airports[ticket[0]] = airports.get(ticket[0], []) + [ticket[1]]
    # airports =  {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
    for airport in airports:
        airports[airport].sort()
    # airports = {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

    visited = {}
    for key, value in airports.items():
        visited[key] = [0] * len(value)
    # visited = {'ICN': [0, 0], 'SFO': [0], 'ATL': [0, 0]}

    path = ['ICN']
    result = []
    def DFS(start):
        nonlocal result

        if result:
            return

        if len(path) == len(tickets) + 1:
            result = path[:]
            return

        # start = icn
        # solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]) 
        # 인천 - B - 인천 - A면 성립하는데, 인천 - A 로 가면 성립이 안되버리니까 조건 추가
        # if start in airports:
        #     for index, dest in enumerate(airports[start]):
        #         # dest = atl, sfo 
        #         if visited[start][index] == 0:
        #             visited[start][index] = 1
        #             path.append(dest)
        #             DFS(dest)
        #             visited[start][index] = 0
        #             path.pop()
        for index, dest in enumerate(airports.get(start, [])):
            if visited[start][index] == 0:
                visited[start][index] = 1
                path.append(dest)
                DFS(dest)
                visited[start][index] = 0
                path.pop()

    DFS(path[0])
    print(airports)
    return result


# 테스트 1 〉	실패 (런타임 에러)
# 테스트 2 〉	실패 (런타임 에러)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	실패 (0.02ms, 10.1MB)

# def solution(tickets):
#     airports = {}
#     dep_list = []
#     for ticket in tickets:
#         departure, destination = ticket[0], ticket[1]
#         if departure not in dep_list:
#             dep_list.append(departure)
#             airports[departure] = [destination]
#         else:
#             airports[departure].append(destination)
#     print("airports: ", airports)
    
#     # key값에 해당되는 value꺼내서 정렬하고 첫번째 값 꺼내서 리스트에 넣고 다음 키로 정하기
#     result = []
#     departure = tickets[0][0]
#     while airports:
#         result.append(departure)
#         desti_list = airports[departure]
#         desti_list.sort()
#         destination = desti_list.pop(0)
#         # airports[departure] = desti_list
        
#         if len(desti_list) == 0:
#             airports.pop(departure)
#         departure = destination
    
#     result.append(destination)
#     print(result)
#     return result

# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]) # 인천 - B - 인천 - A면 성립하는데, 인천 - A 로 가면 성립이 안되버림