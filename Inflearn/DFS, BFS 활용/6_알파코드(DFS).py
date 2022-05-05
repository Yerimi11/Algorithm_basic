import sys
input = sys.stdin.readline

# 아스키 : chr(x)
# 0 입력되면 입력 종료

def DFS(L):
    global num, cnt, res
    if L == len(num):
        cnt += 1
        if len(res) > len(num):
            res.pop(0)
            res.pop(0)
        print("".join(res))
        return
    a = int(num[L])
    b = int("".join(num[L:L+2]))

    if 0 < a < 10:
        res.append(chr(a+64))
        DFS(L+1)
    if 9 < b < 27:
        res.pop()
        res.pop()
        res.append(chr(b+64))
        DFS(L+2)
    
if __name__ == "__main__":
    num = list(str(input()).rstrip())
    res = []
    cnt = 0
    DFS(0)
    print(cnt)