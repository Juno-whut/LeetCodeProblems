import unittest

class Solution:
    def buyChoco(self, prices, money) -> int:
        min1, min2 = 101, 101 # the contraints of the problem limits prices highest number to 100
        for i in prices:
            if min1 > i:
                min2 = min1
                min1 = i
            elif min2 > i:
                min2 = i
        if (min1 + min2) <= money:
            return money - (min1+min2)
        return money



class SolutionTest(unittest.TestCase):
    def test_case1(self):
        prices = [1,3,2]
        money = 4
        self.assertEqual(Solution().buyChoco(prices, money), 1)

    def test_case2(self):
        prices = [4,3,2,2]
        money = 4
        self.assertEqual(Solution().buyChoco(prices, money), 0)
    
    def test_case3(self):
        prices = [1,6,3,1,2,5]
        money = 20
        self.assertEqual(Solution().buyChoco(prices, money), 18)
    
if __name__ == "__main__":
    unittest.main()