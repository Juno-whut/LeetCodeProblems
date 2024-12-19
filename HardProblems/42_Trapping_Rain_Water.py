import unittest


class Solution:
    def trap(self, height) -> int:
        if len(height) < 3:
            return 0
        
        tallest = max(height)
        collected_water = self.forward(height, tallest)
        collected_water2 = self.backward(height, tallest)
        if collected_water and collected_water2:
            return collected_water + collected_water2
        elif collected_water:
            return collected_water 
        return collected_water2

    def forward(self, height, tallest):
        collected_water = 0
        tallest_stack1 = [height[0]]
        for i in range(1, len(height)):
            
            if height[i] == tallest:
                return collected_water

            if height[i] < tallest_stack1[-1]:
                collected_water += tallest_stack1[-1] - height[i]
            else:
                tallest_stack1.append(height[i])
    
    def backward(self, height, tallest):
        collected_water = 0
        tallest_stack2 = [height[-1]]
        for i in range(len(height)-2, -1, -1):
        
            if height[i] == tallest:
                return collected_water

            if height[i] < tallest_stack2[-1]:
                collected_water += tallest_stack2[-1] - height[i]
            else:
                tallest_stack2.append(height[i])
        
        

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