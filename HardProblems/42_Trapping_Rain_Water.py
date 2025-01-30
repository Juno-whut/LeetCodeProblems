import unittest


class Solution:
    def trap(self, height) -> int:
        height_len = len(height)
        rainwater = 0
        # find biggest number index
        BNI = 0
        for i in range(height_len):
            if height[i] > height[BNI]:
                BNI = i
        
        # iterate forwards 
        biggest = height[0]
        for i in range(0, BNI, 1):
            if height[i] > biggest:
                biggest = height[i]
            else:
                rainwater += biggest - height[i]

        # iterate backeards
        biggest = height[-1]
        for i in range(height_len-1, BNI, -1):
            if height[i] > biggest:
                biggest = height[i]
            else:
                rainwater += biggest - height[i]
        
        return rainwater
        
        

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

    def test2(self):
        self.assertEqual(Solution().trap([4,2,0,3,2,5]), 9)

    def test3(self):
        self.assertEqual(Solution().trap([1,2]), 0)
    
    def test4(self):
        self.assertEqual(Solution().trap([4,2,0,3,2,4,3,4]), 10)


if __name__ == '__main__':
    unittest.main()



"""
add helper method 

helper method takes 2 inputs the array and the current index
helper method then iterates through array from the current index to the
end of the array in worst case, but stops when it finds a number that is
greater than or equal to the current index. If it does not find a number 
greater than or equal to the current index, it returns False and continues 
and skips to the next index.
"""