import sys
read_file = open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/1. 가장 큰 수/in5.txt", 'r')
input = read_file.readline
# input = sys.stdin.readline
n, m = map(int, input().split())
count = m
listN = list(str(n))
output = []
lenN = len(listN)

while lenN > 0:
    if len(output) == 0:
        output.append(listN.pop(0))
        continue

    if output[-1] >= listN[0]:
        output.append(listN.pop(0))
    else:
        output.pop()
        count -= 1

    if len(listN) == 0:
        for _ in range(count):
            output.pop()
        break
    elif count == 0:
        for i in listN:
            output.append(i)
        break

print(*output, sep = '')
