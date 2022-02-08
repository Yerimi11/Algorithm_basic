import sys
input = sys.stdin.readline
n, mix = int(input()), input().rstrip()
nums, temp = [], []

for i in mix:
    if i.isdigit() == True:
        temp.append(i)
    else:
        if len(temp) > 0:
            nums.append(int(''.join(temp)))
            temp = []

print(sum(nums))

# 13으로 잘려야하는데 1, 3으로 잘려서 합이 29->20으로 출력돼서 오류남. -> join으로 해결
