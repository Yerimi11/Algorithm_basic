# 한 배열에 대한 조합을 해주는 combinations 모듈과 각 원소의 중복 갯수를 세주는 counter 모듈이 사용됩니다.

# course의 숫자만큼 반복(2,3,5의 경우, 2개짜리 조합, 3개짜리 조합, 5개짜리 조합 찾기):
# 모든 order에 대해 반복:
# order에 대해 course 값(2개,3개,5개...) 만큼 조합
# (order: A,B,C,F,G / course: 2)의 경우 AB, AC, AF, AG, BC, BF...
# 'XY'와 'YX' 등의 경우를 위해 미리 정렬해준뒤 조합(예제 3번의 경우)
# 조합된 주문(메뉴 'A' + 메뉴 'Z' :'AZ') 에 대해 모든 주문 내역에 있는 해당 조합(ex.'AZ')의 갯수를counter모듈을 이용하여 셈. 
# 해당 counter에 아무 값도 없거나(해당 주문 조합이 나온적이 없었거나), 최댓값이 1이면(해당 조합을 주문한 사람이 혼자라면) 패스
# 아니면 answer에 최댓값(현재 갯수에 해당하는 메뉴 조합 중 가장 많이 주문되었던 것) 을 가진 주문 조합을 다 넣음

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c) # 튜플 형식으로 반환 = ('X', 'Y')
            temp += combi
        course_set = Counter(temp)
        if len(course_set) != 0 and max(course_set.values()) != 1:
            # answer 리스트 + 리스트(튜플을 조인)
            # course_set 딕셔너리를 순회하는데, course_set 딕셔너리의 값들 중 가장 큰 값과 코스셋[x]의 밸류 값이 같다면 answer에 더해라
            # answer += [''.join(x) for x in course_set if course_set[x] == max(course_set.values())]
            
            max_value = max(course_set.values())
            for order_combi, order_combi_cnt in course_set.items():
                if order_combi_cnt == max_value:
                    answer.append(''.join(order_combi))
            
    return sorted(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) # ["AC", "ACDE", "BCFG", "CDE"]