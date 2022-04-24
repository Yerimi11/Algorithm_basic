import sys
from collections import deque
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/7. 교육과정 설계/in2.txt", 'r')
# input = sys.stdin.readline
subs = list(input().rstrip())
n = int(input())
lst = []
for i in range(n):
    lst.append(list(input().rstrip()))

# 필수과목(subs)와 lst의 과목이 일치하면 subs에서 pop해간다. 
# 만약 subs가 비었으면 필수과목을 순서대로 다 넣은 것이므로, YES를 출력한다.
for i in range(n):
    Q = deque(subs)
    for x in lst[i]:
        if len(Q) == 0:
            continue
        if Q[0] == x:
            Q.popleft()
    if len(Q) == 0:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
            
# in2.txt 예시에서
# AKDEF
# 5
# AYKGDHEJ
# AQKWDERTFYP
# CTFKSBDEA
# ASKGHDEF
# WOPASFKGHDEF <- 여기서 중간에 필수과목 중 하나인 F가 먼저 나와버리면 안된다.