# 정렬을 안하게되면 시간복잡도는 n^2이 됨
# 정렬 -> for문 -> i보다 큰 수가 몇 개 있는지 체크하고, 
# 인용횟수(citations[i]) == 전체 리스트 길이 - 큰 수 갯수. 그 수를 return

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