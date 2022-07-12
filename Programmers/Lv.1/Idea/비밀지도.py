# n^2 최대 256 ?
# 그래프는 DFS, BFS인지 먼저 체크
# 10진수를 n자리 2진수로 바꾼 후 그래프로 만들 것
# 1 인덱스 visited 체크 -> #으로 최종 출력

def solution(n, arr1, arr2):
    
    # 10 -> 2
    lst_b = []
    for i in range(n):
        binary = []
        a = arr2[i]
        for _ in range(n):
            b = a%2
            binary.append(b)
            a = a//2
        binary = binary[::-1]
        lst_b.append(binary)
        
    lst_a = []
    for i in range(n):
        binary = []
        a = arr1[i]
        for _ in range(n):
            b = a%2
            binary.append(b)
            a = a//2
        binary = binary[::-1]
        lst_a.append(binary)
        
    g = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if lst_a[i][j] == 0:
                g[i][j] = ' '
            else:
                g[i][j] = '#'
    for i in range(n):
        for j in range(n):
            if lst_b[i][j] == 1:
                g[i][j] = '#'
    
    for i in range(n):
        a = ''.join(g[i])
        g[i] = a
        
    print(g)
    return g
        

# 너무 긴 듯? 반복 되는 부분을 더 간단하게 줄여보자.