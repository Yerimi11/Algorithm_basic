def solution(n, m, x_axis, y_axis):
    board = [list([0]*(n+1) for _ in range(m+1))]
    res = []

    board[]


    res.append(넓이)
    return


solution(4, 4, [1], [3]) # 9
# solution(3, 4, [2], [1,2]) # 4

def solution(n, m, x_axis, y_axis):
  answer = 0

  x_nums = x_axis + [n]
  y_nums = y_axis + [m]

  x_left = 0
  for x_right in x_nums:
    width = x_right - x_left

    y_left = 0
    for y_right in y_nums:
      height = y_right - y_left
      answer = max(answer, width * height)
      y_left = y_right
    
    x_left = x_right

  return answer

# input 이 어느 변을 자르겠다는 정보
# 그러면 예를 들어 1번 예시에서 x 축을
# 길이가 4인 x 축에서 x=1일때 한번 자르겠다고 하면
# 변은 총 2개가 생기지 0~1, 1~4
# y축도 마찬가지로 x=3일때 한번 자르니까 0~3, 3~4
# 내가 확인해야 하는 직사각형 덩어리의 총 개수는 4개지
# 그래서 이중 반복문으로
# 각 변에 따라서 직사각형 넓이를 계산하고 최댓값만 추려서 출력

# 코드
# x축을 1에서 한번 자른다고 했으니까
# 각 변의 꼭지점 정보를 담고 있는 리스트 하나를 만들어서 그걸 이용해서 각각의 변의 길이를 구하면 되겠구나
# 예를 들면 x_nums = [0, 1, 4] (0은 필요없을 듯 하여 코드엔 뺌)