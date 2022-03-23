# 커서를 중심으로 스택을 두 개
# 시간복잡도 O(N) : for문 N번 * 데크 O(1)
import sys
from collections import deque
input = sys.stdin.readline
chars = list(str(input()).rstrip())
n = int(input())

q_l = deque(chars)
q_r = deque()

for i in range(n):
    I = input().rstrip()
    if I == "L":
        if q_l:
            q_r.appendleft(q_l.pop())
    elif I == "D":
        if q_r:
            q_l.append(q_r.popleft())
    elif I == "B":
        if q_l:
            q_l.pop()
    else:
        q_l.append(I[-1])

res = ''.join(q_l+q_r)
print(res)


# 시간초과 O(n^2) : for문 n번연산 * pop, insert가 인덱스를 찾느라 n번 연산
# 최악의 경우 : 길이 10만(반복문 도는 횟수), 명령어의 갯수 50만이니까 pop, insert를 사용해야하는 명령어가 50만개가 들어올 수도 있다
# 10만 * 50만 하면 ..... 최악

# import sys
# input = sys.stdin.readline
# chars = list(str(input()).rstrip())
# n = int(input())

# c = len(chars)
# for i in range(n):
#     I = input().rstrip()
#     if I == "L":
#         if c > 0 :
#             c -= 1
#     elif I == "D":
#         if c < len(chars):
#          c += 1
#     elif I == "B":
#         if c > 0 :
#             c -= 1
#             chars.pop(c)
#     else:
#         chars.insert(c,I[-1])
#         c += 1       

# print(''.join(chars))
 
