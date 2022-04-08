import sys
input = sys.stdin.readline
mixlst = [list(map(int, input().split())) for _ in range(10)]

cards = list(range(1, 21))

while len(mixlst) != 0:
    a, b = mixlst.pop(0)
    # for _ in range((b//a)+1):    # (b-a+1) // 2 로 하면, 밑에 if문 (남은 카드 수가 홀수일 때) 없애도 됨.
        # if a == b or (a-1) == b: # 그리고 두번째 케이스에서 틀려버림.
        #     continue
    for _ in range((b-a+1)//2):
        cards[a-1], cards[b-1] = cards[b-1], cards[a-1]
        a, b = a+1, b-1

for i in cards:
    print(i, end = ' ')

# 5 10
# 9 13
# 1 2
# 3 4
# 5 6
# 1 2
# 3 4
# 5 6
# 1 20
# 1 20

# 답 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20

# 13 17
# 2 19
# 1 2
# 3 19
# 1 1
# 1 9
# 11 16
# 5 6
# 1 3
# 1 9
# 답 19 1 2 4 3 5 8 7 6 9 15 16 17 12 11 10 14 13 18 20