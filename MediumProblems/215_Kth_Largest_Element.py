import unittest


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort()
        nums.reverse()
        return nums[k-1]


class TestFindKthLargest(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findKthLargest([3,2,1,5,6,4], 2), 5)
    
    def test2(self):
        self.assertEqual(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)


if __name__ == '__main__':
    unittest.main()

"""
Im choosing to sort and then ill come back after i learn how a heap queue works 
"""