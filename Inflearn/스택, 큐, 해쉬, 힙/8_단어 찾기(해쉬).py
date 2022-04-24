import sys
# sys.read=open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/8. 단어찾기/in1.txt", 'r')
input = sys.stdin.readline
n = int(input())
# 해쉬문제
poetry = dict()
# 단어들을 key값으로, val를 1로 설정해둔 후, 쓰인 단어들의 val를 0으로 바꿔 체크
for i in range(n):
    word = input()
    poetry[word] = 1
for i in range(n-1):
    word = input()
    poetry[word] = 0

for key, val in poetry.items():
    if val == 1:
        print(key)
        break