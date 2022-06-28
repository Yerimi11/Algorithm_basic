from collections import defaultdict

def solution(s):
    # 딕셔너리
    # 횟수 제일 많은 key값을 순서대로 출력
    lst = [s.split(',') for s in s[2:-2].split('},{')]
    
    dict = defaultdict(int)

    for i in lst:
        for j in i:
            dict[j] += 1
    
    k_temp = []
    v_temp = []
    answer = []
    for k, v in dict.items():
        k_temp.append(k)
        v_temp.append(v)
    
    for _ in range(len(dict)):
        a = v_temp.index(max(v_temp))
        v_temp[a] = -1
        answer.append(int(k_temp[a]))
    return answer