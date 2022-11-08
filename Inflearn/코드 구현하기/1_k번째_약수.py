import sys

n, k = map(int, sys.stdin.readline().split())
cnt = 0

for i in range(1, n+1):
    if n % 1 == 0:
        cnt += 1
    if cnt == k: # count가 k번째 약수를 찾았을 때
        print(i)
        break
    
# k번째 약수를 찾지 못했을 때
#for-else문 (for문이 정상적으로 끝난 이후(약수를 찾지 못하고 끝난 경우))
else: 
    print(-1)
        