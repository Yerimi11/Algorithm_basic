import sys
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/9. 아나그램(구글)/in1.txt", "r")
word1 = input()
word2 = input()

# ASCII 코드 숫자를 이용해 계산
check1 = [0] * 52
check2 = [0] * 52

for x in word1:
    if x.isupper():
        check1[ord(x)-65] += 1 # 대문자 해싱
    else:
        check1[ord(x)-71] += 1 # 소문자 해싱

for x in word2:
    if x.isupper():
        check2[ord(x)-65] += 1
    else:
        check2[ord(x)-71] += 1

for i in range(52):
    if check1[i] != check2[i]:
        print("NO")
        break
else:
    print("YES")