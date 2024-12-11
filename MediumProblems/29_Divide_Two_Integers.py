import unittest



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31

        negatives = 2
        subtractions = 0

        if dividend == -MIN_INT and (divisor == -1):
            return MAX_INT

        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        
        while( dividend - divisor <= 0):
            dividend -= divisor
            subtractions -= 1
        
        if negatives == 1:
            return subtractions
        elif negatives == 2:
            subtractions = -subtractions
            return subtractions
        return -subtractions



class TestDivide(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().divide(10, 3), 3)
    
    def test2(self):
        self.assertEqual(Solution().divide(7, -3), -2)

    def test3(self):
        self.assertEqual(Solution().divide(-31, 3), -10)
    
    def test4(self):
        self.assertEqual(Solution().divide(1,1), 1)




if __name__ == '__main__':
    unittest.main()