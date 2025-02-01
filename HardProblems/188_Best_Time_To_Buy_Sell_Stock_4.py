import unittest


class Solution:
    def maxProfit(self, k: int, prices) -> int:
        pass



  

class TestMaxProfit(unittest.TestCase):
    def leet1(self):
        self.assertEqual(Solution().maxProfit(2, [2,4,1]), 2)
    
    def leet2(self):
        self.assertEqual(Solution().maxProfit(2, [[3,2,6,5,0,3]]), 7)
        
    def test1(self):
        self.assertEqual(Solution().maxProfit(2, [3,3,5,0,0,3,1,4]), 6) 
    
    def test2(self):
        self.assertEqual(Solution().maxProfit(2, [1,2,3,4,5]), 4) # Stricly increasing

    def test3(self):
        self.assertEqual(Solution().maxProfit(2, [7,6,4,3,1]), 0) # Stricly decreasing

    def test4(self):
        self.assertEqual(Solution().maxProfit(2, [6,1,3,2,4,7]), 7)



if __name__ == '__main__':
    unittest.main()