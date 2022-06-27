from collections import defaultdict

def solution(s):
    # 딕셔너리
    # 횟수 제일 많은 key값이 맨 앞 튜플 수로 출력
    lst = [s.split(',') for s in s[2:-2].split('},{')]
    
    dict = defaultdict(int)

    for i in lst:
        for j in i:
            dict[j] += 1
    print("dict", dict)
    
    k_temp = []
    v_temp = []
    answer = []
    for k, v in dict.items():
        k_temp.append(k)
        v_temp.append(v)
    print("k_temp", k_temp)
    print("v_temp", v_temp)
    
    for _ in range(len(dict)):
        a = v_temp.index(max(v_temp))
        v_temp[a] = -1
        answer.append(int(k_temp[a]))
    return answer


    # temp.sort(reverse=True)
    # print("temp", temp)
    
    # r_dict = {v:k for k,v in dict.items()}
    # for x in temp:
    #     r_dict.get(x)
        
        # a = temp.index(max(temp)) + 1
        # k = dict.index(a)
        # answer.append()
        # temp[-1] = -1

