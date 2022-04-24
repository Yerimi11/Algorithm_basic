import sys
import heapq as hq
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/스택,큐,해쉬,힙/10. 최소힙/in1.txt", "r")
nums = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(nums) == 0:
            print(-1)
        else:
            print(-hq.heappop(nums))
    else:
        hq.heappush(nums, -n)