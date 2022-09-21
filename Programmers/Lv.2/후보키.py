# 테스트케이스 추가
# [["a", "1", "aaa", "c", "ng"], ["a", "1", "bbb", "e", "g"], ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]  >>>> 5
# [["a", "aa"], ["aa", "a"], ["a", "a"]]  >>>> 1
# [["100", "100", "ryan", "music", "2"], ["200", "200", "apeach", "math", "2"], ["300", "300", "tube", "computer", "3"], ["400", "400", "con", "computer", "4"], ["500", "500", "muzi", "music", "3"], ["600", "600", "apeach", "music", "2"]] >>>> 3
# [["a", "1", "aaa", "c", "ng"], ["b", "1", "bbb", "c", "g"], ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]  >>>>> 3

# https://school.programmers.co.kr/learn/courses/30/lessons/42890#

[["a", "1", "aaa", "c", "ng"], 
 ["a", "1", "bbb", "e", "g"], 
 ["c", "1", "aaa", "d", "ng"], 
 ["d", "2", "bbb", "d", "ng"]]  >>>> 5
(1,3), (1,4), (1,5), (2,4), (3,4)
# (1,2,3), (1,3,4).. 이런 것 다 되지만 최소 갯수여야하니 pass

# 최소성 검사를 먼저 한다. for in 으로, 후보키 후보들 중에서 최소성 검사로 먼저 제외함
#   (ex:(1)이 후보키를 만족했을 때, (1,3), (1,2,4) 이런 것들은 볼 필요가 없어짐. 이미 (1)이 최소 후보키니까
# 다음으로 유일성 검사. combination으로 열(인덱스) 조합(튜플)을 찾아낸다. 조합 갯수는 1개부터(학번 하나로도 되니까)
# for문으로 행을 돌면서 열 조합에 나온 행의 인덱스를 해쉬 키-밸류로 넣어서 len을 비교

# 최소성 검사를 먼저 한다. for in 으로, 후보키 후보들 중에서 최소성 검사로 먼저 제외함
#   (ex:(1)이 후보키를 만족했을 때, (1,3), (1,2,4) 이런 것들은 볼 필요가 없어짐. 이미 (1)이 최소 후보키니까
# 다음으로 유일성 검사. combination으로 열(인덱스) 조합(튜플)을 찾아낸다. 조합 갯수는 1개부터(학번 하나로도 되니까)
# for문으로 행을 돌면서 열 조합에 나온 행의 인덱스를 해쉬 키-밸류로 넣어서 len을 비교

from itertools import combinations


# 최소성 검사 먼저
def is_minimal(candidate_keys, x):
    for i in range(len(candidate_keys)):
        for ck in candidate_keys[i]:
            if ck not in x:
                break
        else:
            return False
    return True

# 유일성 검사
def is_unique(relation, combi):
    hash_list = set()
    for row in range(len(relation)):
        for c in combi: # c: (0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), ...
            hash_list.add(relation[row][c])
        combi_cnt_total = len(combi) * len(relation)
        if combi_cnt_total == len(hash_list):
            return True
        else:
            return False
        
    
def solution(relation):
    a = 1
    n_row = len(relation)
    n_col = len(relation[0])
    
    combi_list = []
    for i in range(1, n_col+1):
        combi_list.extend(combinations(range(n_col), i))
        # combi_list = [(0,), (1,), (2,), (3,), 
                    #   (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), 
                    #   (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]
    
    candidate_keys = []
    for combi in combi_list:
        if is_minimal(candidate_keys, combi) and is_unique(relation, combi):
            candidate_keys.append(combi)
            
    
    return len(candidate_keys)

solution([["a", "1", "aaa", "c", "ng"],  ["a", "1", "bbb", "e", "g"],  ["c", "1", "aaa", "d", "ng"],  ["d", "2", "bbb", "d", "ng"]]) # 5


# --------------------------------------

# from itertools import combinations


# def solution(relation):
#     n_row = len(relation)
#     n_col = len(relation[0])

#     candidate = list()
#     for i in range(1, n_col+1):
#         candidate.extend(combinations(range(n_col), i))  #종목별로 만들 수 있는 모든 조합갯수 찾기

#     final = []
#     for keys in candidate:
#         tmp = [tuple([item[key] for key in keys]) for item in relation] # 주어진 키로 리스트의 index별 아이템 뽑아내기
#         if len(set(tmp)) == n_row: #set로 변경후 사라진게 없다면 key로 사용해도 무방
#             final.append(keys)

#     print(final)
#     answer = set(final[:])
#     print("answer", answer)
#     for i in range(len(final)):
#         for j in range(i+1, len(final)):
#             if len(final[i]) == len(set(final[i]).intersection(set(final[j]))): # key 중에 겹치는 부분이 있는 것을 삭제
#                 answer.discard(final[j])
#     return(len(answer))



# # ---------------------------

# from itertools import combinations

# def solution(relation):
#     columnSize = len(relation[0])
#     CandidateKeys = []
#     answer = 0
#     columnIdx = [i for i in range(columnSize)]

#     for size in range(1, columnSize + 1):
#         columnCombis = combinations(columnIdx, size)
#         nowSet = set()
#         isCandidateKey = True

#         for columnCombi in columnCombis:
#             # 최소성 확인
#             minimal = True
#             for CandidateCol in CandidateKeys:
#                 including = True
#                 for col in CandidateCol:
#                     if col not in columnCombi:
#                         including = False
#                         break

#                 if including:
#                     minimal = False
#                     break

#             #최소성을 만족하지 못하면 건너 뛴다
#             if not minimal:
#                 continue

#             #유일성 확인
#             nowSet = set()
#             isCandidateKey = True
#             for row in relation:
#                 #해당하는 컬럼의 값을 하나의 값으로 만든다
#                 nowVal = ""
#                 for idx in columnCombi:
#                     nowVal += ',' + row[idx]

#                 #동일한 값이 있다면 유일성을 만족하지 못한다
#                 if nowVal in nowSet:
#                     isCandidateKey = False
#                     break
#                 else:
#                     nowSet.add(nowVal)

#             #최소성과 유일성을 만족하면 후보키이다
#             if isCandidateKey:
#                 answer += 1
#                 CandidateKeys.append(columnCombi)

#     return answer
