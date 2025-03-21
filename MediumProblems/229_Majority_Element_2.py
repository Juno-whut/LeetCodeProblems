import unittest


class Solution1:
    def majorityElement(self, nums: list[int]) -> list[int]:
        po1, po2, count1, count2 = None, None, 0, 0
        for num in nums:
            if num == po1:
                count1 += 1
            elif num == po2:
                count2 += 1
            elif count1 == 0:
                po1 = num
                count1 = 1
            elif count2 == 0:
                po2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        for p in [po1, po2]:
            if nums.count(p) > len(nums)//3:
                res.append(p)
        return res
           
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        majority = len(nums)//3
        occurs = {}
        for num in nums:
            if num not in occurs:
                occurs[num] = 0 
            occurs[num] += 1
        
        ans = []
        for k, v in occurs.items():
            if v > majority:
                ans.append(k)
        return ans
                


class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.s = Solution().majorityElement

    def test_1(self):
        self.assertEqual(self.s([3, 2, 3]), [3])

    def test_2(self):
        self.assertEqual(self.s([1, 1, 1, 3, 3, 2, 2, 2]), [1, 2])




if __name__ == '__main__':
    unittest.main()