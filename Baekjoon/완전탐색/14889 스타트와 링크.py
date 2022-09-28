import sys

def cal_diff(team1, team2):
    sum_team1 = 0
    sum_team2 = 0

    for i in range(len(team1)):
        for j in range(len(team1)):
            sum_team1 += arr[team1[i]][team1[j]]
            sum_team2 += arr[team2[i]][team2[j]]

    return abs(sum_team1 - sum_team2)

def make_team(team1, count, N, start):
    global answer

    if count == N//2:
        team2 = []
        for i in range(N):
            if i not in team1:
                team2.append(i)

        local_diff = cal_diff(team1, team2)
        answer = min(answer, local_diff)
        return

    for i in range(start, N):
        if i not in team1:
            team1.append(i)
            make_team(team1, count+1, N, i+1)
            team1.remove(i)

if __name__=="__main__":
    input = sys.stdin.readline
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 2147000000
    make_team([], 0, N, 0)

    print(answer)

# 재귀, 브루트포스


# -------------------------------------------------------------

# import sys
# from itertools import permutations
# input = sys.stdin.readline
# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# for i in range(n):
#     for j in range(n):
#         graph[i][j]

# # 1~n명이 n//2명으로 나누어 팀을 할 수 있는 순열을 구한다
# # i,j로 그래프를 돌며 두 팀의 각 점수 합을 구한 후, 두 팀 점수의 차이가 최소일때를 갱신해 출력한다.
# # 45m + 풀이 참고

# # 여기서 이렇게 순열을 구하면 두 팀으로 나눌 때 실제 사람 번호는 안나눠지는 문제가 있다
#     # -> 잘못 접근했다.
# # 예-> 1,2,3,4,5,6 일 때 1,2,5 / 3,4,6 으로 딱 둘로 나눠서 못구한다. 경우의 수 순열만 구해질 뿐
# mem_num = n//2 
# members_li = []
# members_li = list(permutations(graph[0], mem_num))
# # print(members_li)

# # 6
# # 0 1 2 3 4 5
# # 1 0 2 3 4 5
# # 1 2 0 3 4 5
# # 1 2 3 0 4 5
# # 1 2 3 4 0 5
# # 1 2 3 4 5 0
# # [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 2, 1), (0, 2, 3), (0, 2, 4), (0, 2, 5), (0, 3, 1), (0, 3, 2), (0, 3, 4), (0, 3, 5), (0, 4, 1), (0, 4, 2), (0, 4, 3), (0, 4, 5), (0, 5, 1), (0, 5, 2), (0, 5, 3), (0, 5, 4), (1, 0, 2), (1, 0, 3), (1, 0, 4), (1, 0, 5), (1, 2, 0), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 0), (1, 3, 2), (1, 3, 4), (1, 3, 5), (1, 4, 0), (1, 4, 2), (1, 4, 3), (1, 4, 5), (1, 5, 0), (1, 5, 2), (1, 5, 3), (1, 5, 4), (2, 0, 1), (2, 0, 3), (2, 0, 4), (2, 0, 5), (2, 1, 0), (2, 1, 3), (2, 1, 4), (2, 1, 5), (2, 3, 0), (2, 3, 1), (2, 3, 4), (2, 3, 5), (2, 4, 0), (2, 4, 1), (2, 4, 3), (2, 4, 5), (2, 5, 0), (2, 5, 1), (2, 5, 3), (2, 5, 4), (3, 0, 1), (3, 0, 2), (3, 0, 4), (3, 0, 5), (3, 1, 0), (3, 1, 2), (3, 1, 4), (3, 1, 5), (3, 2, 0), (3, 2, 1), (3, 2, 4), (3, 2, 5), (3, 4, 0), (3, 4, 1), (3, 4, 2), (3, 4, 5), (3, 5, 0), (3, 5, 1), (3, 5, 2), (3, 5, 4), (4, 0, 1), (4, 0, 2), (4, 0, 3), (4, 0, 5), (4, 1, 0), (4, 1, 2), (4, 1, 3), (4, 1, 5), (4, 2, 0), (4, 2, 1), (4, 2, 3), (4, 2, 5), (4, 3, 0), (4, 3, 1), (4, 3, 2), (4, 3, 5), (4, 5, 0), (4, 5, 1), (4, 5, 2), (4, 5, 3), (5, 0, 1), (5, 0, 2), (5, 0, 3), (5, 0, 4), (5, 1, 0), (5, 1, 2), (5, 1, 3), (5, 1, 4), (5, 2, 0), (5, 2, 1), (5, 2, 3), (5, 2, 4), (5, 3, 0), (5, 3, 1), (5, 3, 2), (5, 3, 4), (5, 4, 0), (5, 4, 1), (5, 4, 2), (5, 4, 3)]


# # i,j로 그래프를 돌며 두 팀의 각 점수 합을 구한 후, 두 팀 점수의 차이가 최소일때를 갱신해 출력한다.
# min_sum = 2147000000
# team_sum_li = []
# # 팀 멤버가 3명 이상이면?
# for combi in members_li:
#     team_sum = 0
#     for i in range(len(combi)):
#         for j in range(i, len(combi)):
#             team_sum += graph[i][j]
#         team_sum_li.append(team_sum)
#     min_sum = min(min(team_sum_li), min_sum)

# print(min_sum)

# # 두 팀의 능력치 차이의 최솟값을 출력한다

# .
# .