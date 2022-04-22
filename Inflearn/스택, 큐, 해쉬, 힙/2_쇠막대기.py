import sys
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/2. 쇠막대기/in5.txt", 'r')
# input = sys.stdin.readline
a = str(input().rstrip())
a = list(map(str, a))
stack = []
count = 0

for i in range(len(a)):
    if a[i] == '(':         # stack에 (를 쌓는다 - 쇠막대기 시작
        stack.append(a[0])
    else:
        stack.pop()
        if a[i-1] == '(':   # () 레이저 일 때 stack에서 (를 pop한다
            # stack.pop()
            count += len(stack)
        else:
            # stack.pop()     # 레이저가 지나간 후 쇠막대기가 끝나는 )이면 쇠막대기 시작이었던 (를 pop하고
            count += 1      # 이미 잘린 쇠막대기 count를 더한다.
            
print(count)
