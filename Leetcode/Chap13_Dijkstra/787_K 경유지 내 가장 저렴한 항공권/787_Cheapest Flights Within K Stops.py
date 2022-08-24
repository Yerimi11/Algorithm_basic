class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # k번 경유해서 갈 수 있는 src->dst 거리의 최소 비용
        
        # (비용, 목적지) 순서로 힙에 넣는다
        