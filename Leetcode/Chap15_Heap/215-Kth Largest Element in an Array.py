class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
            # nums.heapify() 후, 최소힙으로 정렬(최댓값이 루트에 오도록) 
            # for i in range(): 로 루트 빼주며 최소힙 정렬(자동), 
            # k번째까지 빼준 후 k번째가 될 때의 루트 값을 return
            heapq.heapify(nums)
            
            for i in range(len(nums)-k): # 작은수부터 정렬되는데, K번째로 큰 수니 뒤에서 k번째 수를 구하면 됨
                heapq.heappop(nums)
            
            return heapq.heappop(nums)