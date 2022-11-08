import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

result = set()
for i in range(n):
    #j는 for문 i의 다음것 부터 n의 전까지 돈다
    for j in range(i+1, n):
        #m는 for문 j의 다음것 부터 n의 전까지 돈다
        for m in range(j+1, n):
        # 이렇게 삼중for문을 돌리면
        # i  j  (m) (m) (m) m이 순서대로 돌아서
        # 1  2   3   4   5  => 123, 124, 125, ...
        # 그 다음은 j가 뒤로(3으로) 가서 134, 135, 145, ..
            result.add(a[i]+a[j]+a[m])

# set자료구조는 sort가 안돼서 우선 리스트화 한다
result = list(result)
# 내림차순 정렬
result.sort(reverse=True)
# k번째 출력
print(result[k-1])
        