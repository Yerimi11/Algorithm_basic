import sys

# 현재 값이 우측으로 이동하면서 저점과 차이 계산
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 한 번의 거래로 낼 수 있는 최대 이익 산출
        # 앞에서부터 작은 날에 사고 뒤에 높은 날에 팔기.. 오늘이 작은 줄 어떻게 알고? -> 리스트 값 다 계산해서 차이 보고 결정. min과 max구하기 (순서대로)
        profit = 0
        min_price = sys.maxsize
        
        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit
        
        # 시간복잡도 O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 현재 값이 우측으로 이동하면서 저점과 차이 계산
        min_ = float('inf')
        diff = 0
        for i in range(len(prices)):
            curr = prices[i]
            # if min_ > curr:
            #     min_ = curr
            min_ = min(min_, curr)
            
            temp = curr - min_
            # if temp > diff:
            #     diff = temp
            diff = max(temp, diff) # 비교문 안쓰고 한 줄로 정리 가능!
        return diff