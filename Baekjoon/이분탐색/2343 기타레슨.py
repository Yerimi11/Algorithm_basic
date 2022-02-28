# 순서대로 블루레이를 만들어야하고, M개로 나뉘어야하며, 1개의 블루레이에는 최소 2개의 강의가 들어가야한다. 출력은 강의 길이의 합 중 max값을 출력해야 한다.

# 이분탐색 문제, 두번째 줄의 리스트 숫자들을 두 개로 나누면서 temp에 저장해 비교한다.
# 예를 들면, 우선 left, mid, right를 만들고,
# 9개의 숫자를 3등분할 때, right부터 2개씩 자르며 옮기면서 mid값 갱신(?)
# left~mid값의 합은 temp에 저장해두고 ㄴ 이 위에 2개씩 자른 것의 합과 비교…?

# —

# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# lessons = list(map(int, input().split()))

# 이 문제는 이분 탐색(Binary Search) 문제이다.
# 주어진 기타 레슨을 M개 이하의 구역으로 분리하는 블루레이 크기 중 최솟값을 출력하면 된다.

# 이분 탐색을 진행하기 위해서 Left, Right를 아래와 같이 초기화하였다.
# Left = sum(기타 레슨) // M    => left  15 = 45%3
# Right = sum(기타 레슨)        => right 45
# answer(최종답) = Right       => answer 45


# 위 과정을 진행한 후 본격적인 이분 탐색 과정은 다음과 같다.
# 1. mid값을 구한다. (left + right) // 2        => mid 30 = (15+45)//2
# 2. mid값이 기타 레슨의 최댓값보다 작은지 판단한다.
#    -  작다면 기타 레슨을 담을 수 없으므로 left = mid + 1로 업데이트한다.          => left 31
# 3. mid값으로 기타 레슨을 M개 이하의 구역으로 나눌 수 있는지 판단한다.               => 31 % 3 쌉가능
#    - 나눌 수 있다면 더 작은 값을 판단하기 위해서 right = mid - 1로 업데이트한다.   => right 29
#    - answer값보다 mid값이 작다면 answer를 mid로 업데이트한다.                 => answer 30
#    - 나눌 수 없다면 더 큰 값을 판단하기 위해서 left = mid + 1로 업데이트한다.

if __name__ == "__main__":

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    lesson_total = sum(arr)
    left, right = lesson_total // M, sum(arr)
    # print(left, right)
    answer = right
    while left <= right:
        mid = (left + right) // 2

        if mid < max(arr):
            left = mid + 1
            continue
        # 조건 만족 확인
        count, temp = 0, 0
        for i in range(len(arr)):
            if arr[i] > mid:
                break
            elif temp + arr[i] <= mid:
                temp += arr[i]
            else:
                temp = arr[i]
                count += 1

        if count <= M - 1:  # 가능한 경우 (더 작은 값이 있는지 확인해야 한다)
            right = mid - 1
            answer = min(answer, mid)  # answer 값 업데이트
        else:  # 값을 증가시켜야 한다.
            left = mid + 1

    print(answer)
