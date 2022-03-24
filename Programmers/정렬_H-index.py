def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()    # [0, 1, 3, 5, 6]
    
    for i in range(n):
        hIndex = n-i # H-index
        if citations[i] >= hIndex:
            answer = hIndex
            break
    return answer
# https://gurumee92.tistory.com/177


# 정렬을 안하게되면 시간복잡도는 n^2이 됨
# 정렬 -> for문 -> i보다 큰 수가 몇 개 있는지 체크하고, 
# 작은 수 == 전체 리스트 길이 - 큰 수 갯수 그 수를 return => 항상 같은 값 나오므로 의미X

# def solution(citations):
#     answer = []
#     length = len(citations)
#     citations.sort()    # [0, 1, 3, 5, 6]
    
#     for i in range(length-1):
#         count = 0
#         count += len(citations[i+1:length])
#         if len(citations[0:i+1]) == length - count:
#             answer.append(i)
#     return max(answer)

# 정렬을 안하게되면 시간복잡도는 n^2이 됨
# 정렬 -> for문 -> i보다 큰 수가 몇 개 있는지 체크하고, 
# 인용횟수(citations[i]) == 전체 리스트 길이 - 큰 수 갯수. 그 수를 return

# def solution(citations):
#     answer = []
#     n = len(citations)
#     citations.sort()    # [0, 1, 3, 5, 6]
    
#     for i in range(n):
#         # if citations[i] == n - len(citations[i+1:n]):
#         count = 0
#         count += len(citations[i+1:n])
#         if citations[i] <= (n - count) and citations[i] > len(citations[0:i]):
#             answer.append(citations[i])
#     print(answer)
#     return max(answer)
        
        