import sys
# input = sys.stdin.readline
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/문자열&1,2차원리스트탐색/10. 스도쿠 검사/in5.txt", 'r')

G = []
for _ in range(9):
    G.append(list(map(int, input().split())))
    
# 1. 가로, 세로 1줄씩은 그 1줄을 임시리스트에 담아서 set()화 하여 중복을 없앤 후, 그 리스트의 길이가 9인지 확인한다!
# 2. 3x3칸은 2중 for문 3번 3번 돌려서 G[i][j]를 sum에 더하여 3x3의 총 합이 45가 아니면 "NO" 출력

temp = set()
for ix in range(9):
    for jx in range(9):
        temp.add(G[ix][jx])
    if len(temp) != 9:
        print("No")
        sys.exit()
    temp = set()

for iy in range(9):
    for jy in range(9):
        temp.add(G[jy][iy])
    if len(temp) != 9:
        print("No")
        sys.exit()
    temp = set()

# 여기서도 sum이 아니라 set 사용해도 될 듯?
sum = 0
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        sum += G[i][j] + G[i+1][j] + G[i+2][j]
        sum += G[i][j+1] + G[i+1][j+1] + G[i+2][j+1]
        sum += G[i][j+2] + G[i+1][j+2] + G[i+2][j+2]
        if sum != 45:
            print("No")
            sys.exit()
        sum = 0

print("Yes")