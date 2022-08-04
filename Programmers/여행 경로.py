# 테스트 1 〉	실패 (런타임 에러)
# 테스트 2 〉	실패 (런타임 에러)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	실패 (0.02ms, 10.1MB)

def solution(tickets):
    airports = {}
    dep_list = []
    for ticket in tickets:
        departure, destination = ticket[0], ticket[1]
        if departure not in dep_list:
            dep_list.append(departure)
            airports[departure] = [destination]
        else:
            airports[departure].append(destination)
    print("airports: ", airports)
    
    # key값에 해당되는 value꺼내서 정렬하고 첫번째 값 꺼내서 리스트에 넣고 다음 키로 정하기
    result = []
    departure = tickets[0][0]
    while airports:
        result.append(departure)
        desti_list = airports[departure]
        desti_list.sort()
        destination = desti_list.pop(0)
        # airports[departure] = desti_list
        
        if len(desti_list) == 0:
            airports.pop(departure)
        departure = destination
    
    result.append(destination)
    print(result)
    return result

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])