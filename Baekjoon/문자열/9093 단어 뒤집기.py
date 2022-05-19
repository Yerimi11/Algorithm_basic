n = int(input())
for i in range(n):
    word = list(map(str, input().split()))
    res = ''
    for j in range(len(word)):
        res += word[j][::-1]
        res += ' '
    print(res)
