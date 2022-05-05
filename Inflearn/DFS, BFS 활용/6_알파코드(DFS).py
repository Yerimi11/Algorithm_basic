import sys
input = sys.stdin.readline

# 아스키 : chr(x)
# 0 입력되면 입력 종료

def DFS(L):
    global cnt, res
    if L == len(num):
        if len(res) > len(num):
            res = res[2:]   # pop, slicing 둘 다 O(N). pop(0)을 2번 하면, 2N이니까 슬라이싱 사용. pop(0)을 O(1)로 하려면 deque사용하면 됨
        print("".join(res))
        cnt += 1
        return
    a = int(num[L])
    b = int("".join(num[L:L+2]))

    if 0 < a < 10:
        res.append(chr(a+64))
        DFS(L+1)
    if 9 < b < 27:
        res = res[:-2]
        res.append(chr(b+64))
        DFS(L+2)
    
if __name__ == "__main__":
    num = list(str(input()).rstrip())
    res = []
    cnt = 0
    DFS(0)
    print(cnt)