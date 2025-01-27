import unittest


class Solution:
    def getCommon(self, nums1, nums2) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        common_elements = set1.intersection(set2)
        if not common_elements:
            return -1  
        return min(common_elements)


class TestGetCommon(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().getCommon([1, 2, 3], [2, 4]), 2)
    
    def test2(self):
        self.assertEqual(Solution().getCommon([1, 2, 3], [2, 4, 6]), 2)


if __name__ == '__main__':
    unittest.main()