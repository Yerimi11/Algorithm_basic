def solution(id_list, report, k):
    answer = []
    return answer

# 유저아이디는 해쉬테이블(딕셔너리)로 {아이디:신고횟수} 구조로 만들어 놓자
# report->set으로 동일 인물 동일 신고 제외
# repost[i].split()으로 분리 되는지, 되면 report[i][1]의 신고 수 += 1 카운팅 해줌(딕셔너리)
# 출력에서 k는 관련이 없는 것 같고, 딕셔너리 value값 전부를 최종 리턴해준다.
# 해시테이블의 시간복잡도는 O(1) ?