import sys
# sys.read=open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/9. 아나그램(구글)/in2.txt", 'r')
input = sys.stdin.readline
word1 = input()
word2 = input()
check = dict()

for x in word1:
    check[x] = check.get(x, 0) + 1

for x in word2:
    check[x] = check.get(x, 0) - 1

for x in word1:
    if check.get(x) > 0:
        print("NO")
        break
else:
    print("YES")