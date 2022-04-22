import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/5. 공주구하기/in5.txt", 'r')
# input = sys.stdin.readline
n, k = map(int, input().split())
queue = []

for i in range(n):
    queue.append(i+1)

while len(queue) > 1:
    for i in range(k):
        queue.append(queue.pop(0))
        if i == k-1:
            queue.pop()

print(*queue)