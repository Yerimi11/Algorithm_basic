# 순서대로 블루레이를 만들어야하고, M개로 나뉘어야하며, 1개의 블루레이에는 최소 2개의 강의가 들어가야한다. 출력은 강의 길이의 합 중 max값을 출력해야 한다.

# 이분탐색 문제, 두번째 줄의 리스트 숫자들을 두 개로 나누면서 temp에 저장해 비교한다.
# 예를 들면, 우선 left, mid, right를 만들고,
# 9개의 숫자를 3등분할 때, right부터 2개씩 자르며 옮기면서 mid값 갱신(?)
# left~mid값의 합은 temp에 저장해두고 ㄴ 이 위에 2개씩 자른 것의 합과 비교…?

# —

# 이 문제는 이분 탐색(Binary Search) 문제이다.
#  
# 주어진 기타 레슨을 M개 이하의 구역으로 분리하는 블루레이 크기 중 최솟값을 출력하면 된다.
#  
# 이분 탐색을 진행하기 위해서 Left, Right를 아래와 같이 초기화하였다.
# Left = sum(기타 레슨) // M
# Right = sum(기타 레슨)
# answer(최종답) = Right
#  
# 위 과정을 진행한 후 본격적인 이분 탐색 과정은 다음과 같다.
# 1. mid값을 구한다. (left + right) // 2
# 2. mid값이 기타 레슨의 최댓값보다 작은지 판단한다.
#    -  작다면 기타 레슨을 담을 수 없으므로 left = mid + 1로 업데이트한다.
# 3. mid값으로 기타 레슨을 M개 이하의 구역으로 나눌 수 있는지 판단한다.
#    - 나눌 수 있다면 더 작은 값을 판단하기 위해서 right = mid - 1로 업데이트한다.
#    - answer값보다 mid값이 작다면 answer를 mid로 업데이트한다.
#    - 나눌 수 없다면 더 큰 값을 판단하기 위해서 left = mid + 1로 업데이트한다.
