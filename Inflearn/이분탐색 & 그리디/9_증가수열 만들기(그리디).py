import sys
from collections import deque
read_file = open("/Users/yerim/Downloads/pythonalgorithm_formac/이분탐색&그리디/9. 증가수열 만들기/in5.txt", 'r')
input = read_file.readline
n = int(input())
nums = list(map(int, input().split()))
nums = deque(nums)
LR = ""
temp = []
# 왼, 오 비교해서 더 작은 값 가져오는데, 그 수가 이미 만들어진 증가수열의 맨 끝 값보다 커야 함. 
# 그리고 가져오는 원소 위치에 따라 L, R 기록
# 최종 증가수열 원소의 갯수 카운팅
temp.append(0)
while nums:
    if len(nums) == 1 and temp[-1] > nums[0]:
        if (nums[0] > int(temp[-1])):
            LR += 'L'
        break
    if (nums[0] < nums[-1]):
        if (nums[0] > int(temp[-1])):
            LR += 'L'
            temp.append(nums.popleft())
        elif (nums[-1] > int(temp[-1])):
            LR += 'R'
            temp.append(nums.pop())
        else:
            break
    elif (nums[0] > nums[-1]):
        if (nums[-1] > int(temp[-1])):
            LR += 'R'
            temp.append(nums.pop())
        elif (nums[0] > int(temp[-1])):
            LR += 'L'
            temp.append(nums.popleft())
        else:
            break

print(len(temp)-1)
print(LR)

read_file.close()