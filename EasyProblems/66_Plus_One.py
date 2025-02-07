import unittest



class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits



class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.s = Solution().plusOne

    def test_plusOne(self):
        self.assertEqual(self.s([1, 2, 3]), [1, 2, 4])
    
    def test1(self):
        self.assertEqual(self.s([4, 3, 2, 1]), [4, 3, 2, 2])
    
    def test2(self):
        self.assertEqual(self.s([0]), [1])
    
    def test3(self):
        self.assertEqual(self.s([9]), [1, 0])



if __name__ == '__main__':
    unittest.main()
