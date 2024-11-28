import unittest

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        if k == 0:
            return False
        
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            if len(seen) == k:
                seen.remove(nums[i-k])
            seen.add(nums[i])
        return False





class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3, 1]
        k = 3
        self.assertTrue(Solution().containsNearbyDuplicate(nums, k))

    def test_2(self):
        nums = [1, 0, 1, 1]
        k = 2
        self.assertTrue(Solution().containsNearbyDuplicate(nums, k))

    def test_3(self):
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        self.assertFalse(Solution().containsNearbyDuplicate(nums, k))



if __name__ == "__main__":
    unittest.main()