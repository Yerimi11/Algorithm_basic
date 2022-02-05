a, b, c= map(int, input().split())
print((a if a<b else b) if ((a if a<b else b) < c) else c)

# 처음에 a b 비교하고 그 값 중 작은 것 비교 
# 그 다음 그 값과 남은 c 중 작은 값을 비교
