# 풀이 참고함. 

from copy import deepcopy
max_diff, max_board = 0, []
def solution(n, info):
    def dfs(ascore, lscore, cnt, idx, board):
        global max_diff, max_board
        if cnt > n:
            return
        if idx > 10:
            diff = lscore - ascore
            if diff > max_diff:
                board[10] = n - cnt
                max_board = board
                max_diff = diff
            return
        if cnt < n:
            board2 = deepcopy(board); board2[10-idx] = info[10-idx] + 1
            dfs(ascore, lscore+idx, cnt+info[10-idx]+1, idx+1, board2)
            
        board1 = deepcopy(board)
        
        if info[10-idx] > 0:
            dfs(ascore+idx, lscore, cnt, idx+1, board1)            
        else:
            dfs(ascore, lscore, cnt, idx+1, board1)
            
    dfs(0, 0, 0, 0, [0]*11)
    return max_board if max_board else [-1]



solution(5,[2,1,1,1,0,0,0,0,0,0,0]) # [0,2,2,0,1,0,0,0,0,0,0]

    # 라이언이 이기기로 마음 먹은 점수에서는 어피치보다 딱 1개 더 맞추고, 
    # 이기지 않기로 마음먹은 점수에서는 0개를 맞춘 후 
    # 남은 화살은 전부 0점에 몰아주기
    
    # DFS를 이용한 완전 탐색으로 풀이를 진행하겠습니다.

    # 이 문제를 해결하기 위해서는 각 점수를 아예 안 맞추거나 어피치보다 1발을 더 맞히는 경우로 각 점수(10점 ~ 0점)마다 2가지(총 2048가지)를 완전 탐색하면 됩니다.

    # 예를 들어, 어피치가 [2,0,1,1,0,0,0,0,0,0,0]처럼 화살을 맞췄을 경우 라이언은 과녁 점수 10점을 3발 맞추거나 0발 맞추거나만 선택하면 됩니다. 9점~0점도 동일한 방식으로 어피치보다 1발을 더 맞추거나 아예 안 맞추도록 구현하면 되고, 중간에 화살을 다 쐈을 경우는 나머지 과녁 점수를 모두 0발 맞춘 것으로 처리하면 됩니다. 만약 1점까지 쏘고도 화살이 남았을 경우는 남은 화살을 0점에 다 쏘도록 처리할 수 있습니다. 이렇게 가능한 모든 경우를 살펴보면서 라이언과 어피치의 최대 점수 차이를 구하면 됩니다.

    # 만약 10점부터 0점까지를 0발부터 n발까지 하나씩 증가시키면서 완전탐색한다면 최악의 경우 시간 초과가 발생할 수 있는 점 유의하시길 바랍니다.
    