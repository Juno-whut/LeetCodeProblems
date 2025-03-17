import unittest



class Solution:
    def maxArea(self, height: list[int]) -> int:
        biggest_area = 0
        max_height = max(height)
        left = 0
        right = len(height)-1

        while left < right:
            if max_height * (right - left) < biggest_area:
                return biggest_area
            
            temp_min = min(height[left], height[right])
            temp_product = temp_min * (right - left)
            if temp_product > biggest_area:
                biggest_area = temp_product
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return biggest_area



class testMaxArea(unittest.TestCase):
    def setUp(self):
        self.s = Solution().maxArea
    
    def test1(self):
        self.assertEqual(self.s([1,8,6,2,5,4,8,3,7]),49)
    
    def test2(self):
        self.assertEqual(self.s([1,1]), 1)
    
    def test3(self):
        self.assertEqual(self.s([1,2,4,3]), 4)


if __name__ == '__main__':
    unittest.main()