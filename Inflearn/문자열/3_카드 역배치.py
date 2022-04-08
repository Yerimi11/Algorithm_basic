import sys
input = sys.stdin.readline
mixlst = [list(map(int, input().split())) for _ in range(10)]

cards = list(range(1, 21))

while len(mixlst) != 0:
    a, b = mixlst.pop(0)
    for _ in range((b//a)+1): # (b-a+1) // 2 로 하면, 밑에 if문 (남은 카드 수가 홀수일 때) 없애도 됨
        if a == b or (a-1) == b:
            continue
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