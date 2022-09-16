# 테스트케이스 추가
# [["a", "1", "aaa", "c", "ng"], ["a", "1", "bbb", "e", "g"], ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]  >>>> 5
# [["a", "aa"], ["aa", "a"], ["a", "a"]]  >>>> 1
# [["100", "100", "ryan", "music", "2"], ["200", "200", "apeach", "math", "2"], ["300", "300", "tube", "computer", "3"], ["400", "400", "con", "computer", "4"], ["500", "500", "muzi", "music", "3"], ["600", "600", "apeach", "music", "2"]] >>>> 3
# [["a", "1", "aaa", "c", "ng"], ["b", "1", "bbb", "c", "g"], ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]  >>>>> 3

# https://school.programmers.co.kr/learn/courses/30/lessons/42890#

def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)