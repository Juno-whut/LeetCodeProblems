import unittest



class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices: 
            return 0

        sell1, sell2 = 0, 0
        buy1, buy2 = 9999999999, 9999999999

        for price in prices:
            if price < buy1:
                buy1 = price
            if price - buy1 > sell1:
                sell1 = price - buy1

            if price - sell1 < buy2:
                buy2 = price - sell1
            if price - buy2 > sell2:
                sell2 = price - buy2
        
        return sell2

        
        



'''
class Solution:
    def maxProfit(self, prices):
        currentLow = prices[0]
        MaxProfit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < currentLow:
                currentLow = prices[i]
            elif i+2 <= len(prices):
                if prices[i+1] <= prices[i]:
                    MaxProfit += prices[i] - currentLow
                    currentLow = prices[i]
            else:
                MaxProfit += prices[i] - currentLow
        
        return MaxProfit
'''




class MaxProfitTest(unittest.TestCase):
    def test_case1(self):
        prices = [7,1,5,3,6,4]
        self.assertEqual(Solution().maxProfit(prices), 7)

    def test_case2(self):
        prices = [7,6,4,3,1]
        self.assertEqual(Solution().maxProfit(prices), 0)
    
    def test_case3(self):
        prices = [1,2,3,4,5]
        self.assertEqual(Solution().maxProfit(prices), 4)
    
    def test_case4(self):
        prices = [1]
        self.assertEqual(Solution().maxProfit(prices), 0)

if __name__ == '__main__':
    unittest.main()