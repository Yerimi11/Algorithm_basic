import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/4. 후위식 연산/in5.txt", 'r')
# input = sys.stdin.readline
num = input().rstrip()
# num = list(map(str, num))
stack = []

for x in num:
    if x.isdecimal():   # 숫자이면
        stack.append(int(x))
    else:
        if len(stack) >= 2:
            if x == '*':
                stack.append(stack.pop(-2)*stack.pop())
            elif x == '/':
                stack.append(stack.pop(-2)/stack.pop())
            elif x == '+':
                stack.append(stack.pop(-2)+stack.pop())  
            else:
                stack.append(stack.pop(-2)-stack.pop())
print(stack)