# [
#     [0,0,0,0,0],
#     [0,0,1,0,3],
#     [0,2,5,0,1],
#     [4,2,4,4,2],
#     [3,5,1,3,1]
#     ]

def solution(board, moves):
    # 모든 i열에서 moves j인덱스를 탐색, 0은 pass하다가 
    # 0이 아닌 숫자가 나오면 0으로 바꾼 후 바구니 스택에 넣는다. 
    # 스택[-1]과 바구니에 넣을 숫자가 같다면 둘 다 pop후 cnt += 2
    basket = []
    cnt = 0
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                basket.append(board[i][m-1])
                board[i][m-1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        cnt += 2
                break
            
    return cnt


