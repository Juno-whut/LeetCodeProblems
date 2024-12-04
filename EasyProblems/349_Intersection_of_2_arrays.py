import unittest

class Solution:
    # def intersection(self, nums1, nums2):
    #     unique_map = {}
    #     for i in nums1:
    #         unique_map[i] = 1

    #     for i in nums2:
    #         if i in unique_map:
    #             unique_map[i] = 2

    #     return_list = []
    #     for k, v in unique_map.items():
    #         if v >= 2:
    #             return_list.append(k)
    #     return return_list

    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
                

class TestIntersection(unittest.TestCase):
    def test_intersection(self):
        self.assertEqual(Solution().intersection([1,2,2,1], [2,2]), [2])
    
    def test2(self):
        self.assertEqual(Solution().intersection([4,9,5], [9,4,9,8,4]), [9,4])

if __name__ == '__main__':
    unittest.main()