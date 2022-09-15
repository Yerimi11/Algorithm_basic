# 소수는 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수

# 진법 변환
def convert(n, k):
    power = 0
    tmp = ""
    while n:
        tmp = str(n%k) + tmp
        n //= k
    return tmp

def isPrime(n): # 소수 판별 함수
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    # k진수로 바꾸고, 변환한 수를 탐색
    # 탐색 중 앞 뒤에 0이 붙은 1보다 큰 숫자가 10진수 기준으로 소수이면 list에 넣기
    # list 원소 갯수를 리턴
    result = []
    k_num = convert(n, k) # k진수로 변환한 숫자
    temp = ""
    for i, x in enumerate(k_num):
        if int(x) > 0:
            temp += x
        if int(x) == 0 or i == len(k_num)-1:
            if temp and int(temp) != 1 and isPrime(int(temp)) == True:
                result.append(temp)
            temp = ""
    return len(result)

solution(437674, 3)