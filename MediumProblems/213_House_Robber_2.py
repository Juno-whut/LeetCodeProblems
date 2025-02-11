import unittest


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max1, max2, prev1, prev2 = 0, 0, 0, 0

        for i in range(0, len(nums)-1):
            temp = 0
            if max1 > (prev1 + nums[i]):
                temp = max1
            else:
                temp = prev1 + nums[i]
            prev1 = max1
            max1 = temp
        
        for i in range(1, len(nums)):
            temp = 0
            if max2 > (prev2 + nums[i]):
                temp = max2
            else:
                temp = prev2 + nums[i]
            prev2 = max2
            max2 = temp
        
        return max(max1,max2)



class TestRob(unittest.TestCase):
    def setUp(self):
        self.s = Solution().rob
    
    def test1(self):
        self.assertEqual(self.s([1,2,3]), 3)
    
    def test2(self):
        self.assertEqual(self.s([1,2,3,4]), 6)
    
    def test3(self):
        self.assertEqual(self.s([1]), 1)
    
    def test4(self):
        self.assertEqual(self.s([2,3,2]), 3)
    
    def test5(self):
        self.assertEqual(self.s([1,2,3,4,5,6]), 12)
    
    def test6(self):
        self.assertEqual(self.s([200,3,140,20,10]), 340)
    
    def test7(self):
        self.assertEqual(self.s([1,3,1,3,100]), 103)


if __name__ == '__main__':
    unittest.main()