import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/문자열&1,2차원리스트탐색/11. 격자판 회문수/in5.txt", 'r')

G = [list(map(int, input().split())) for _ in range(7)]

# 가로 탐색, 세로 탐색 한 줄 씩 리스트에 넣고, 5자리 회문 발견하면 cnt += 1
# 회문 확인 방법은 3cases가 있다. OOOOOXX, XOOOOOX, XXOOOOO
# 출발 인덱스 [0],[4] / [1],[5] / [2],[6] 를 검사하면 된다. [i], [i+4]
#  ㄴ 같으면 [j+1], [j-1] 이렇게 줄여나가며 회문인지 검사한다.

cnt = 0
temp = []

for ix in range(7):
    for jx in range(7):
        temp.append(G[ix][jx]) # 가로줄 1줄씩 넣음
    for x in range(3):         # 회문 검사
        if temp[x] == temp[x+4]:
            if temp[x+1] == temp[x+3]:
                cnt += 1
    temp = []

for iy in range(7):
    for jy in range(7):
        temp.append(G[jy][iy])  # 세로줄 1줄씩 넣음
    for x in range(3):          # 회문 검사
        if temp[x] == temp[x+4]:   
            if temp[x+1] == temp[x+3]:
                cnt += 1
    temp = []

print(cnt)