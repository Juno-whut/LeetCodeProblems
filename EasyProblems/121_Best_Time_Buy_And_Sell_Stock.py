import unittest


class Solution:
    def maxProfit(self, prices):
        LN = prices[0]
        MaxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < LN:
                LN = prices[i]
            elif (prices[i] - LN) > MaxProfit:
                MaxProfit = prices[i] - LN
        
        return MaxProfit



class MaxProfitTest(unittest.TestCase):
    def test_case1(self):
        prices = [7,1,5,3,6,4]
        self.assertEqual(Solution().maxProfit(prices), 5)

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