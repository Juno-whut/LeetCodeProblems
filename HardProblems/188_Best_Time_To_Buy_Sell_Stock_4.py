import unittest


class Solution:
    def maxProfit(self, k: int, prices) -> int:
        currentLow = prices[0]
        MaxProfit = 0
        maxSells = k
        
        if len(prices) == 1:
            return 0
        
        for i in range(1, len(prices)):
            if maxSells == 0:
                return MaxProfit
            if prices[i] < currentLow:
                currentLow = prices[i]
            else:
                MaxProfit += prices[i] - currentLow
                currentLow = prices[i]
                maxSells -= 1
        
        return MaxProfit



  

class TestMaxProfit(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().maxProfit(2, [3,3,5,0,0,3,1,4]), 6)
    
    def test2(self):
        self.assertEqual(Solution().maxProfit(2, [1,2,3,4,5]), 4)

    def test3(self):
        self.assertEqual(Solution().maxProfit(2, [7,6,4,3,1]), 0)

    def test4(self):
        self.assertEqual(Solution().maxProfit(2, [6,1,3,2,4,7]), 7)



if __name__ == '__main__':
    unittest.main()