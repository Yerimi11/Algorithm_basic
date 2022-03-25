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
#         a_answer.append(i+1)
#         if i > 0 and b_answer[-1] != 2:
#             b_answer.append(i+1)
#         else:
#             b_answer.append(2)
        
#         if i % 10 == 0 or 1:
#             c_answer.append(3) # 33 11 22 44 55 / 01 23 45 67 89
#         elif i % 10 == 2 or 3:
#             c_answer.append(1)
#         elif i % 10 == 4 or 5:
#             c_answer.append(2)
#         elif i % 10 == 6 or 7:
#             c_answer.append(4)
#         elif i % 10 == 8 or 9:
#             c_answer.append(5)
        if answers[i] == a_answer[(i%5)]:
            counts[0] += 1
        if answers[i] == b_answer[(i%8)]:
            counts[1] += 1
        if answers[i] == c_answer[(i%10)]:
            counts[2] += 1


    # 완전탐색(브루트포스)이니, 컴퓨터의 속도를 믿고 무식하게 전부 다 찾아 볼 것.
    # 맞은 갯수 카운팅
    # for i in range(len(answers)):
    #     if a_answer[i] == answers[i]:
    #         a_count += 1
    #     if b_answer[i] == answers[i]:
    #         b_count += 1
    #     if c_answer[i] == answers[i]:
    #         c_count += 1
    
    # temp = []     # count 중 max값 찾아서 temp에 넣기
    # temp.append(max(a_count, b_count, c_count))
    # answer.append(a_count)
    # answer.append(b_count)    
    # answer.append(c_count)
    
    # 가장 높은 점수를 받은 학생은 전부 다 출력해야하니까, max값과 학생 번호(i+1)이 같은지 찾는다
    for i in range(3):
        if counts[i] == max(counts): # count max값 여기서 찾는 걸로 수정. 
            answer.append(i+1)
    
    return answer





# def solution(answers):
#     answer = []     # 1, 2, 3번 수포자 중 가장 많은 정답을 맞힌 사람의 번호 삽입
#     # 1, 2, 3번 수포자의 정답 갯수를 담기
#     a_count = 0     # 1 2 3 4 5 순서대로 반복하는 규칙
#     b_count = 0     # 1 3 4 5 앞에 2를 넣는 규칙
#     c_count = 0     # 3 1 2 4 5 두 번씩 반복하는 규칙
#     a_answer = []
#     b_answer = []
#     c_answer = []
    
#     # 수포자들이 찍은 번호 배열
#     for i in range(len(answers)):
#         a_answer.append(i+1)
#         if i > 0 and b_answer[-1] != 2:
#             b_answer.append(i+1)
#         else:
#             b_answer.append(2)
        
#         if i % 10 == 0 or 1:
#             c_answer.append(3) # 33 11 22 44 55 / 01 23 45 67 89
#         elif i % 10 == 2 or 3:
#             c_answer.append(1)
#         elif i % 10 == 4 or 5:
#             c_answer.append(2)
#         elif i % 10 == 6 or 7:
#             c_answer.append(4)
#         elif i % 10 == 8 or 9:
#             c_answer.append(5)

#     # 완전탐색(브루트포스)이니, 컴퓨터의 속도를 믿고 무식하게 전부 다 찾아 볼 것.
#     # 맞은 갯수 카운팅
#     for i in range(len(answers)):
#         if a_answer[i] == answers[i]:
#             a_count += 1
#         if b_answer[i] == answers[i]:
#             b_count += 1
#         if c_answer[i] == answers[i]:
#             c_count += 1
    
#     temp = []
#     temp.append(max(a_count, b_count, c_count))
#     answer.append(a_count)
#     answer.append(b_count)    
#     answer.append(c_count)
    
#     # 위치가 여러개가 나올 수 있으니까
#     temp2 = []
#     for i in range(3):
#         temp2.append(answer.index(temp)) # answer의 temp라는 값의 위치를 찾기
    
#     temp2.sort()
#     return temp2