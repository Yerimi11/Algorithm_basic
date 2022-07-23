# begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# https://github.com/Yerimi11/Algorithm_yerim/blob/main/Programmers/Lv.2/%EB%8B%A8%EC%96%B4%20%EB%B3%80%ED%99%98.py
# 복습시 : 어떻게 풀어야 할 지 그림 그리기, Visited가 왜 필요한지 생각

# begin에서 target으로 변환하는 '가장 짧은 변환 과정'을 찾으려고 합니다.
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.

from collections import deque

def solution(begin, target, words):
    # 큐에 넣고 탐색!
    answer = 0
    q = deque()
    q.append((begin, 0))
    words_visited = list([0] * len(words))
    
    while q:
        word, cnt = q.popleft()
        # print("word     : ", word)
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            diff_cnt = 0
            if not words_visited[i]: # False == 0 근데 꼭 있어야 하나? - 순서대로가 아니므로 재탐색 가능성 있으니 필요
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff_cnt += 1
                # words의 낱말 중 begin단어와 한글자만 다를 경우에만 알파벳 교체 가능하므로, 
                if diff_cnt == 1:
                    # 현재 단어와 한 글자만 다른 word들을 depth와 함께 q에 넣어주어 알파벳을 교체할 수 있는 후보로 친다.
                    # 한 글자만 다를 경우 q에 다 들어가기 때문에 계속 바꾸면서 순회하지만, depth는 같으므로 바꾼 횟수에는 영향 X
                    q.append((words[i], cnt+1))
                    # print("q : ", q)
                    words_visited[i] = 1
    
    return answer



solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])

# visited 유무로 속도 차이 20배 남 (있는게 빠름)

# # begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
# # 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# # 2. words에 있는 단어로만 변환할 수 있습니다.

# from collections import deque

# def solution(begin, target, words):
#     # 큐에 넣고 탐색!
#     answer = 0
#     q = deque()
#     q.append((begin, 0))
#     # words_visited = list([0] * len(words))
    
#     while q:
#         word, cnt = q.popleft()
#         # print("word     : ", word)
#         if word == target:
#             answer = cnt
#             break
#         for i in range(len(words)):
#             diff_cnt = 0
#             # if not words_visited[i]: # False == 0 근데 꼭 있어야 하나? (없어도 통과!)
#             for j in range(len(word)):
#                 if word[j] != words[i][j]:
#                     diff_cnt += 1
#             # words의 낱말 중 begin단어와 한글자만 다를 경우에만 알파벳 교체 가능하므로, 
#             if diff_cnt == 1:
#                 # 현재 단어와 한 글자만 다른 word들을 depth와 함께 q에 넣어주어 알파벳을 교체할 수 있는 후보로 친다.
#                 # 한 글자만 다를 경우 q에 다 들어가기 때문에 계속 바꾸면서 순회하지만, depth는 같으므로 바꾼 횟수에는 영향 X
#                 q.append((words[i], cnt+1))
#                 # print("q : ", q)
#                 # words_visited[i] = 1
    
#     return answer

# solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])