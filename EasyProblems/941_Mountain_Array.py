import unittest

class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        arrlen = len(arr)
        if arrlen < 3:
            return False
        
        Increasing, Decreasing = False, False
        prev = arr[0]
        for i in range(1, arrlen):
            if prev == arr[i]:
                return False
            
            if prev < arr[i]:
                if Decreasing:
                    return False
                Increasing = True
                prev = arr[i]
            elif prev > arr[i]:
                if not Increasing:
                    return False
                Decreasing = True
                prev = arr[i]

        return True if Increasing and Decreasing else False




class TestValidMountainArray(unittest.TestCase):
    def setUp(self):
        self.s = Solution().validMountainArray
    
    def test1(self):
        self.assertEqual(self.s([2,1]), False) # Array does not contain 3 or more digits
    
    def test2(self):
        self.assertEqual(self.s([3,5,5]), False) # Array does not decrease / array does not stricly increase then decrease
    
    def test3(self):
        self.assertEqual(self.s([0,3,2,1]), True) # Fuffils all conditions length greater than or equal to 3, strictly increasing then decreasing
    
    def test4(self):
        self.assertEqual(self.s([1,2,3,4,5,6,7,8]), False) # Never Decreases
    
    def test5(self):
        self.assertEqual(self.s([5,4,3,2,1]), False) # Never Increases
    
    def test6(self):
        self.assertEqual(self.s([0,1,2,1,2]), False) # Increase, Decrease, then Increases again


if __name__ == '__main__':
    unittest.main()
