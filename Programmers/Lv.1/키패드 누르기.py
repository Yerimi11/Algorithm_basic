# BFS 재귀로 할 필요 없이, 상하좌우 이동만 하면 된다.
# 3*4 board에서 상하좌우 움직여야하고,
# 현재 왼/오른손 엄지손가락의 위치를 저장해둬야하며
# if 1,4,7,'*' elif 3,6,9,'#' else:
# 2,5,8,0일 때 그 저장위치와 가야할 numbers[i]의 위치와 거리를 계산한다
# 그 후 더 적은 거리인 손가락이 이동하고, 이동한 위치를 다시 저장

key_xy = {'1':(0,0), '2':(0,1), '3':(0,2), '4':(1,0), '5':(1,1), '6':(1,2), '7':(2,0), '8':(2,1), '9':(2,2), '*':(3,0), '0':(3,1), '#':(3,2)}
        
def solution(numbers, hand):
    answer = ''
    L_h = (3,0)
    R_h = (3,2)
    for n in numbers:
        n = str(n)
        L_x, L_y = L_h[0], L_h[1]
        R_x, R_y = R_h[0], R_h[1]
        
        if n == '1' or n == '4' or n == '7' or n == '*':
            L_h = key_xy[n]
            answer += 'L'
            
        elif n == '3' or n == '6' or n == '9' or n == '#':
            R_h = key_xy[n]
            answer += 'R'

        else:
        #     # 왼오 손가락 위치와 이동해야할 키패드와의 i, j 거리 비교 후
        #     # 왼,오 중에 더 거리 가까운 손가락이 움직이고 거리 같다면 hand잡이로 이동 후 손가락 좌표 갱신
            x, y = key_xy[n][0], key_xy[n][1]
            if (abs(L_x-x)+abs(L_y-y)) > (abs(R_x-x)+abs(R_y-y)):
                R_h = key_xy[n]
                answer += 'R'
            elif (abs(L_x-x)+abs(L_y-y)) < (abs(R_x-x)+abs(R_y-y)):
                L_h = key_xy[n]
                answer += 'L'
            else:
                if hand == "right":
                    R_h = key_xy[n]
                    answer += 'R'
                else:
                    L_h = key_xy[n]
                    answer += 'L'
        
    return answer

