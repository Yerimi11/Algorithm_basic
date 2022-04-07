n = int(input())
words = []
for _ in range(n):
    word = str(input())
    word = word.lower()
    words.append(word)

for i in range(len(words)):
    for j in range(len(words)):
        if words[i][j] == words[i][(-j)-1]:
            if j == len(words[i])//2:
                print("YES")
                break
    
        else:
            print("NO")
            break

# 5
# level
# moon
# abcba
# soon
# gooG