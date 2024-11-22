import unittest

class Solution:
    # Solution 1
    def minPartitions(self, n: str):
        ans = 0
        nums = list(n)
        for i in nums:
            if int(i) == 9:
                return 9
            if int(i) > ans:
                ans = int(i)
        return ans


    # Solution 2
    def minPartitions(self, n: str):
        return int(max(n))


class MinPartitionsTest(unittest.TestCase):
    def test_basecase_1(self):
        n = '32'
        self.assertEqual(Solution().minPartitions(n), 3)

    def test_basecase_2(self):
        n = '82734'
        self.assertEqual(Solution().minPartitions(n), 8)
    
    def test_basecase_3(self):
        n = '27346209830709182346'
        self.assertEqual(Solution().minPartitions(n), 9)
    
    def test_1Num(self):
        n = '8'
        self.assertEqual(Solution().minPartitions(n), 8)



if __name__ == '__main__':
    unittest.main()