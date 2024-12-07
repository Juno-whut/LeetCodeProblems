import unittest


class Solution:
    def intersect(self, nums1, nums2):
        nums_dict = {}
        duplicates = []
        for i in nums1:
            if i in nums_dict:
                nums_dict[i] +=1
            else:
                nums_dict[i] = 1
        
        for i in nums2:
            if i in nums_dict:
                if nums_dict[i] > 0:
                    duplicates.append(i)
                    nums_dict[i] -= 1
        return duplicates



class TestIntersect(unittest.TestCase):
    def test_intersect(self):
        self.assertEqual(Solution().intersect([1,2,2,1], [2,2]), [2, 2])
    
    def test_itersect2(self):
        self.assertEqual(Solution().intersect([4,9,5], [9,4,9,8,4]), [9, 4])



if __name__ == '__main__':
    unittest.main()