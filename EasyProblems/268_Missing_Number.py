import unittest


class Solution:
    def missingNumber(self, nums) -> int:
        set_nums = set(nums)
        for i in range(len(nums)):
            if i not in set_nums:
                return i
        return i + 1


class TestMissingNumber(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().missingNumber([0,2,3,1]), 4)

    def test2(self):
        self.assertEqual(Solution().missingNumber([3,0,1]), 2)

    def test3(self):
        self.assertEqual(Solution().missingNumber([9,6,4,2,3,5,7,0,1]), 8)
    

if __name__ == "__main__":
    unittest.main()