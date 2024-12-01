import unittest


class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for nums in nums:
            if count == 0:
                candidate = nums
            if nums == candidate:
                count += 1
            else:
                count -= 1

        return candidate
# class Solution:
#     def majorityElement(self, nums) -> int:
#         n = len(nums) / 2
#         elements = {}

#         for num in nums:
#             if num in elements:
#                 elements[num] += 1
#             else:
#                 elements[num] = 1
        
#         for k, v in elements.items():
#             if v > n:
#                 return k
#         return 0
    

class TestMajorityElement(unittest.TestCase):
    def test_1(self):
        nums = [3, 2, 3]
        self.assertEqual(Solution().majorityElement(nums), 3)

    def test_2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        self.assertEqual(Solution().majorityElement(nums), 2)

    def test_3(self):
        nums = [1]
        self.assertEqual(Solution().majorityElement(nums), 1)

if __name__ == "__main__": 
    unittest.main()
