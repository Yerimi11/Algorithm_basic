a, b = map(float, input().split())
cal = a/b 
cal = round(cal, 4) # 소수 넷째 자리에서 반올림하여
print(f'{cal:.3f}')          # 셋째 자리까지 출력
