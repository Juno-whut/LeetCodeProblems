import unittest


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        ans, running_total, ones_since_0 = 0, 0, 0

        for i in nums:
            if i == 0:
                if ans < running_total:
                    ans = running_total
                running_total = ones_since_0 + 1
                ones_since_0 = 0
            else:
                running_total += 1
                ones_since_0 += 1
        
        return max(ans, running_total)




class TestFindMaxConsecutiveOnes(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
    
    def test1(self):
        self.assertEqual(self.s.findMaxConsecutiveOnes([1,1,1,1,0,1,0,1,1,1,1,1,1]), 8)

    def test2(self):
        self.assertEqual(self.s.findMaxConsecutiveOnes([1,0,1,1,0,1]), 4)
    
    def test3(self):
        self.assertEqual(self.s.findMaxConsecutiveOnes([0,0,0,0,0]), 1)
    
    def test4(self):
        self.assertEqual(self.s.findMaxConsecutiveOnes([1,0,1,1,0]), 4)


if __name__ == "__main__":
    unittest.main()