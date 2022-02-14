2231

맨 앞자리 수는 그 수가 k이면 1~k까지 재귀 다 돌고
그 다음 자리 수는 0~9까지 다 돌면서 재귀로 찾기

"M" == 'a' + 'b' + 'c'
N = M + a + b + c     

import sys
input = sys.stdio.readline
N = int(input())

if len(N) > 2:
	첫글자 뒷글자 나눠서 재귀
	findnum()
	

else: # 1글자일 때
	1~n까지만 돌기
	findnum(N)

def findnum()
	if ("M" == 'a' + 'b' + 'c') and (N = M + a + b + c):
		return M
	 	
	0~9까지 찾기

findnum()


	
