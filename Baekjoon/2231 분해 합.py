# 맨 앞자리 수는 그 수가 k이면 1~k까지 재귀 다 돌고
# 그 다음 자리 수는 0~9까지 다 돌면서 재귀로 찾기

# "M" == 'a' + 'b' + 'c'
# N = M + a + b + c     

import sys
input = sys.stdin.readline

target = int(input())

for i in range(target):
	# target이 245일 때, str화 "245" -> map : 2, 4, 5 더한다
	temp = sum(map(int, str(i))) 
	result = i + temp
	if result == target:
		print(i)
		break
else:
	print(0)

# a = {0,1,2,3,4,5,6,7,8,9}
# b = {0,1,2,3,4,5,6,7,8,9}
# c = {0,1,2,3,4,5,6,7,8,9}

# def findnum(number):
# 	if ("M" == 'a' + 'b' + 'c') and int(N) == (M+a+b+c):
# 		return "M"
		
# 	# 0~9까지 찾기
# 	# [0]	번째 자리만 도는 함수
# 	for i in range(0, fst_num):

# 	# [1:] 번째 자리만 도는 함수
# 	for i in range(0, 10):

# 	return min(M)


# N = str(input()).rstrip()
# fst_num = N[0] 	
# temp = sum(map(int, N))
# if len(N) > 1:
# 	# 첫글자 뒷글자 나눠서 재귀
# 	nums = N[1:]
# 	findnum(fst_num)
# 	findnum(nums)

# else: # 1글자일 때
# 	# 1~n까지만 돌기
# 	findnum(fst_num)

# findnum(N)

