def solution(n, lost, reserve):
    clothes = list([1] * n)
    for i in lost:
        clothes[i-1] -= 1
    for j in reserve:
        clothes[j-1] += 1
    
    for i in range(1, n):
        # 내가 없고 앞에 사람이 있으면 (앞사람이 있을 때, 앞에서 뒤를 줌)
        if clothes[i-1] > 1 and clothes[i] == 0:
            clothes[i-1] -= 1
            clothes[i] += 1
        # 내가 여분을 가지고있고 앞에 친구가 없으면 (앞사람이 없을 때, 뒤에서 앞을 줌)
        elif clothes[i-1] == 0 and clothes[i] > 1:
            clothes[i] -= 1
            clothes[i-1] += 1
    # 왼쪽부터 우측으로 탐색하니까 앞뒤 두번씩 안봐도 괜찮음

    answer = 0    
    for x in clothes:
        if x >= 1:
            answer += 1
    
    return answer

# O(N)