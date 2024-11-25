import unittest

class Solution:
    def canJump(self, nums) -> bool:
        end = len(nums)
        goal = end - 1
        for i in range(end -1, -1, -1):
            max_jump = nums[i] 
            if i + max_jump >= goal:
                goal = i
            if goal == 0:
                return True
        return False


class JumpGameTest(unittest.TestCase):
    def test_basecase_1(self):
        nums = [2,3,1,1,4]
        self.assertTrue(Solution().canJump(nums))

    def test_basecase_2(self):
        nums = [3,2,1,0,4]
        self.assertFalse(Solution().canJump(nums))
    
    def test_basecase_3(self):
        nums = [0]
        self.assertTrue(Solution().canJump(nums))

if __name__ == '__main__':
    unittest.main()