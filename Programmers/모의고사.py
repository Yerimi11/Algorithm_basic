def solution(answers):
    answer = []     # 1, 2, 3번 수포자 중 가장 많은 정답을 맞힌 사람의 번호 삽입
    # 1, 2, 3번 수포자의 정답 갯수를 담기
    # a_count = 0     # 1 2 3 4 5 순서대로 반복하는 규칙
    # b_count = 0     # 1 3 4 5 앞에 2를 넣는 규칙
    # c_count = 0     # 3 1 2 4 5 두 번씩 반복하는 규칙
    # a_answer = []
    # b_answer = []
    # c_answer = []
    counts = [0, 0, 0]
    a_answer = [1, 2, 3, 4, 5]
    b_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    c_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 수포자들이 찍은 번호 배열
    for i in range(len(answers)):
        if answers[i] == a_answer[(i%5)]:
            counts[0] += 1
        if answers[i] == b_answer[(i%8)]:
            counts[1] += 1
        if answers[i] == c_answer[(i%10)]:
            counts[2] += 1
    
    # 가장 높은 점수를 받은 학생은 전부 다 출력해야하니까, max값과 학생 번호(i+1)이 같은지 찾는다
    for i in range(3):
        if counts[i] == max(counts): # count max값 여기서 찾는 걸로 수정. 
            answer.append(i+1)
    
    return answer