arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')
#arrMin = arr[0] 도 ㄱㅊ

for i in range(len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i]
        #같은 수가 중복될 때(2, 2) 앞에 숫자를 가져오거나 뒤에 숫자를 가져오거나 하는 문제라면
        #arr[i]<arrMin에서 <를 <=로 바꿔주면 뒤에껄 넣어서 뒤에꺼 가져올 수 있음
print(arrMin)