# 1) 모든 풀이 과정을 다 리스트에 담아두는 방식으로 접근하지 x
# 2) 입출력 순서에 대한 언급이 있다면, stack , queue 이라 간파하고 pop 으로 풀려고 해보기 

# queue FIFO을 활용한 풀이
def solution(progresses, speeds):

    answer = []
    day = 0
    count = 0
    
    while len(progresses) > 0:
        if (progresses[0] + day * speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)
    return answer

# def solution(progresses, speeds):
#     answer = []
#     days = []
    
#     for i in range(len(progresses)):
#         count = 0
#         day = 1
#         while progresses[i] + (speeds[i] * day) <= 100:
#             if progresses[i] + (speeds[i] * day) == 100:
#                 count += 1
#                 break
#             day += 1
#         days.append(day)

    
#     for i in range(1, len(days)):
#         temp = 0
#         if days[i] < days[i-1]:
#             temp += 1
#         answer.append(temp)
            
        
        
#     # 각 배포마다 몇 개의 기능이 배포되는지를 return
#     return answer