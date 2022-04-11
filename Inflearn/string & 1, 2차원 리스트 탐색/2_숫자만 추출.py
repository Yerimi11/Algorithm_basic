# .isdecimal() 이즈데시멀 - 0~9까지 숫자만 찾아줌
# .isdigit() 이즈디짓 - 해당 문자열이 ‘숫자'로 이루어져 있는지 검사. 2^31 이런 숫자도 찾아줌!

word = input()
nums = ''

for i in word:
    if i.isdecimal() == True:
        nums += i

nums = int(nums)

print(nums)

count = 0
for i in range(1, nums+1):
    if nums % i == 0:
        count += 1
print(count)

# 시간복잡도 -> O(N) : 중첩되는 for문이 없고, 
#                   word길이만큼 돌리는 반복문이 제일 기므로 
#                   word의 길이를 n으로 놓는다면, O(N)
# t0e0a1c2h0er
# 답 120, 16

# g0en2Ts8eSoft
# 답 28, 6