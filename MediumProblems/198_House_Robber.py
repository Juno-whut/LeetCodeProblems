import unittest



class Solution:
    def rob(self, nums) -> int:
        maxScore, prevScore = 0, 0

        for cash in nums:
            temp = 0 
            if maxScore > (prevScore + cash):
                temp = maxScore
            else:
                temp = prevScore + cash
            prevScore = maxScore
            maxScore = temp

        return maxScore         



class TestRob(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().rob([1,2,3,1]), 4)

    def test2(self):
        self.assertEqual(Solution().rob([2,7,9,3,1]), 12)

    def test3(self):
        self.assertEqual(Solution().rob([2,1,1,2]), 4)


if __name__ == "__main__":
    unittest.main()