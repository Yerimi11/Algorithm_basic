import sys
sys.read=open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/9. 아나그램(구글)/in2.txt", 'r')
# input = sys.stdin.readline
word1 = input()
word2 = input()
check1 = dict()
check2 = dict()

for x in word1:
    check1[x] = check1.get(x, 0) + 1

for x in word2:
    check2[x] = check2.get(x, 0) + 1

for i in check1.keys():
    if i in check2.keys():
        if check1[i] != check2[i] # val를 비교
            print("NO")
            break
    else: # 같은 key가 존재하지 않으면
        print("NO")
        break
else:
    print("YES")



# ▣ 입력예제 
# AbaAeCe 
# baeeACA

# ▣ 출력예제 
# YES