import unittest


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        self.memo = {}

        self.memo[0] = 0
        for i in range(1, amount+1):
            self.memo[i] = float('inf')
            for coin in coins:
                subproblem = i - coin
                if subproblem >= 0 and self.memo[subproblem] != float('inf'):
                    self.memo[i] = min(self.memo[i], self.memo[subproblem]+ 1)
        return self.memo[amount] if self.memo[amount] != float('inf') else -1



class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.s = Solution().coinChange
    
    def test1(self):
        self.assertEqual(self.s([1,2,5], 11), 3)
    
    def test2(self):
        self.assertEqual(self.s([3], 1), -1)
    
    def test3(self):
        self.assertEqual(self.s([1,3,5], 0), 0)
    
    def test4(self):
        self.assertEqual(self.s([2,5,10,1], 27), 4)
    

if __name__ == '__main__':
    unittest.main()