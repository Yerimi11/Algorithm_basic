n = int(input())
words = []
for _ in range(n):
    word = str(input())
    word = word.lower()
    words.append(word)

for i in range(len(words)):
    # if words[i] == words[i][::-1]:    # 슬라이싱 이용
    #     print("#%d YES" %(i+1))
    # else:
    #     print("#%d NO" %(i+1))

    for j in range(len(words)):         # 직접 구현
        if words[i][j] == words[i][-j-1]:
            if j == len(words[i])//2:
                print("#%d YES" %(i+1))
                break
    
        else:
            print("#%d NO" %(i+1))
            break

# 5
# level
# moon
# abcba
# soon
# gooG