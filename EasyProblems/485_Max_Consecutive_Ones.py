import unittest


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        currentMax, returnMax = 0 , 0
        
        for num in nums:
            if num == 1:
                currentMax += 1
            
            if currentMax > returnMax:
                returnMax = currentMax

            if num == 0:
                currentMax = 0

        return returnMax

class TestMaxOnes(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findMaxConsecutiveOnes([1,1,1,1,0,1,0,1,1,1,1,1,1]), 6)
    
    def test2(self):
        self.assertEqual(Solution().findMaxConsecutiveOnes([1,0]),1)
    
    def test3(self):
        self.assertEqual(Solution().findMaxConsecutiveOnes([0]), 0)


if __name__ == '__main__':
    unittest.main()