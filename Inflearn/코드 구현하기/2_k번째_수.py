import sys

# n개의 숫자로 이루어진 숫자열
# s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 나오는 k번째 수
t = int(sys.stdin.readline()) # 케이스 갯수 (N)


for testcase in range(t):
    n, s, e, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    #슬라이스는 끝에서-1 해서 끊기니까 e-1번째를 쓰고 싶으면 e로 적어야 함. e번 인덱스 전까지만 출력함.
    a = a[s-1:e]
    a.sort()
    #k번째 숫자 출력
    print("#%d %d" %(testcase+1, a[k-1]))
    #문자 "#'뒤에 t+1출력 >> #%d