def solution(places):
    answer = []
    return answer

# |r1-r2|+|c1-c2|인 맨해튼 거리가 3이상이거나,
# 자리 사이에 파티션이 있으면 OK

# Idea
# 2차원 그래프로 하나씩 for문 돌며 str으로 입력한다.
# 그러면 2중for문을 돌렸을 때 좌표값을 알게 된다.
    # 돌리면서, P가 나오면 temp에 P의 좌표값을 저장해놓고,
    # 다음 P를 찾는 동안 X가 나오면 X좌표값도 저장하고 바로 다음 줄로 넘어간다
    # 다음 줄에서 P가 나왔을 때의 좌표값과 맨해튼 거리를 계산해서
    # 3 미만이고, 위아래행에 X가 없었다면 return result.append(0)
    # 다 패스하면 return result.append(1)
    


[["POOOP", 
  "OXXOX", 
  "OPXPX", 
  "OOXOX", 
  "POXXP"],
 
 
 ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
 ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
 ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
 ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
