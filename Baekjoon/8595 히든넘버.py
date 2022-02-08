import sys
input = sys.stdin.readline
n = int(input())
mix = input().rstrip()

nums, temp = 0, ""
for i in mix:
    if i.isdigit():
        temp += i
        # temp = "23"  
    else:
        if temp:
            nums += int(temp)
            temp = ""

if len(temp) > 0:
   nums += int(temp)
print(nums)

# import sys
# input = sys.stdin.readline
# n = int(input())
# mix = input().rstrip()

# nums, temp = [], []
# for i in mix:
#     if i.isdigit(): # True일 때
#         temp.append(i)
    
#     else:
#         if temp:
#             nums.append(int(''.join(temp)))
#             temp = []

# if len(temp) > 0:
#     nums.append(int(''.join(temp)))
# print(sum(nums))

# 13으로 잘려야하는데 1, 3으로 잘려서 합이 29->20으로 출력돼서 오류남. -> join으로 해결
# 3, 2a3 처럼 마지막에 숫자가 들어올 경우 고려

# 5
# 21a11b21

import sys
input = sys.stdin.readline
n = int(input())
mix = input().rstrip()

nums, temp = 0, "0"
for i in mix:
    if i.isdigit() == True:
        temp += i
    
    else:
        nums += int(temp)
        temp = "0"

print(nums+int(temp))
