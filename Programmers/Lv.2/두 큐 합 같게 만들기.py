from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    mid = (sum1+sum2) // 2 
    cnt = 0
    
    # 길이가 5인 queue1과 queue2에서 
    # 유일한 답이 queue1의 3, 4번째가 한 큐에만 들어가있는 경우
    # 11번의 이동이 필요하다. 이런 케이스도 있기에 *2가 아닌 *3을 해줘야 1번 테케가 통과한다
    for _ in range(len(queue1)*3):
        if sum1 > mid:
            n = queue1.popleft()
            queue2.append(n)
            sum1 -= n
            sum2 += n
            cnt += 1
        elif sum1 < mid:
            n = queue2.popleft()
            queue1.append(n)
            sum2 -= n
            sum1 += n
            cnt += 1
        else:
            return cnt
            break
    
        
    # 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return
    return -1