# 정렬을 안하게되면 시간복잡도는 n^2이 됨
# 정렬 -> for문 -> i보다 큰 수가 몇 개 있는지 체크하고, 
# 인용횟수(citations[i]) == 전체 리스트 길이 - 큰 수 갯수. 그 수를 return

def solution(citations):
    n = len(citations)
    citations.sort()
    
    for i in range(n):
        hIndex = n-i
        if citations[i] >= hIndex:
            return hIndex
    return 0