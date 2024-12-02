import unittest


class Solution:
    def jump(self, nums) -> int:
        jumps, current_end, farthest = 0, 0, 0
        max_index = len(nums)-1
        for i in range(max_index):
            farthest += max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps



class JumpGame2Test(unittest.TestCase):
    def test_basecase_1(self):
        nums = [2,3,1,1,4]
        self.assertEqual(Solution().jump(nums), 2)

    def test_basecase_2(self):
        nums = [2,3,0,1,4]
        self.assertEqual(Solution().jump(nums), 2)

    def test_basecase_3(self):
        nums = [4]
        self.assertEqual(Solution().jump(nums), 0)

if __name__ == '__main__':
    unittest.main()