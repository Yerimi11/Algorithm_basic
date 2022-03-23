# 정렬을 안하게되면 시간복잡도는 n^2이 됨
# 정렬 -> for문 -> i보다 큰 수가 몇 개 있는지 체크하고, 
# 작은 수 == 전체 리스트 길이 - 큰 수 갯수 그 수를 return

def solution(citations):
    answer = []
    length = len(citations)
    citations.sort()    # [0, 1, 3, 5, 6]
    
    for i in range(length-1):
        count = 0
        count += len(citations[i+1:length])
        if len(citations[0:i+1]) == length - count:
            answer.append(i)
    return max(answer)
        