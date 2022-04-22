import sys
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/3. 후위표기식 만들기/in3.txt", 'r')
# input = sys.stdin.readline
# 괄호 먼저 풀어서 연산 괄호의 맨 뒤로 옮기고, 그다음 남은 연산들 맨 뒤로
a = input().rstrip()
stack = []
res = ''

for x in a:
    if x.isdecimal():   # 숫자이면
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()

print(res)


# stack1 = []
# stack2 = []

# for i in range(len(a)):
#     if a[i].isdigit() == False:
#         if a[i] == ')':
#             while stack2[-1] != '(':
#                 stack1.append(stack2.pop())
#             stack2.pop()
#             if len(stack2) > 0 and stack2[-1] == '*':
#                 stack1.append(stack2.pop())
#         elif len(stack2) > 0 and a[i] == '+' or a[i] == '-' and a[i] != '(':
#             while stack2[-1] != '/' or stack2[-1] != '*' or stack2[-1] != '(':
#                 stack1.append(stack2.pop())
#                 if len(stack2) == 0:
#                     stack2.append(a[i])
#                     break
#         else:
#             stack2.append(a[i])
#     else: # 숫자일 때
#         stack1.append(a[i])
#         if len(stack2) > 0 and stack2[-1] == '*':
#             stack1.append(stack2.pop())

# if stack2:
#     for _ in range(len(stack2)):
#         stack1.append(stack2.pop())
    
# print("".join(stack1))